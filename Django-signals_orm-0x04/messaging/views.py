from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def threaded_conversations_view(request):
    # Fetch top-level messages where user is sender or receiver
    messages = Message.objects.filter(
        parent_message__isnull=True
    ).filter(
        sender=request.user
    ).select_related('sender', 'receiver') \
     .prefetch_related('replies__sender', 'replies__receiver')

    return render(request, 'chats/threaded_conversations.html', {'messages': messages})
