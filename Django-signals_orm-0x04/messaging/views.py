from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.cache import cache_page

from .models import Message


@cache_page(60)  # Caching conversation view for 60 seconds
def conversation_view(request):
    messages = Message.objects.select_related('sender', 'receiver') \
        .prefetch_related('replies')
    return render(request, 'chats/conversation.html', {'messages': messages})


@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()  # Required for the check
        return redirect('account_deleted')  # Assumes this URL exists
    return render(request, 'chats/confirm_delete.html')


@login_required
def threaded_conversations_view(request):
    # Top-level messages where the user is the sender
    top_messages = Message.objects.filter(
        sender=request.user,
        parent_message__isnull=True
    ).select_related('sender', 'receiver') \
     .prefetch_related('replies__sender', 'replies__receiver')

    return render(request, 'chats/threaded_conversations.html', {'messages': top_messages})


@login_required
def unread_messages_view(request):
    # Using custom manager and .only() for optimization
    unread_messages = Message.unread.unread_for_user(request.user) \
        .only('id', 'sender', 'content', 'timestamp')

    return render(request, 'chats/unread_messages.html', {'messages': unread_messages})
