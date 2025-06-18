from django.shortcuts import render
from .models import Message
from django.views.decorators.cache import cache_page

@cache_page(60)  # Cache for 60 seconds
def conversation_view(request):
    messages = Message.objects.select_related('sender', 'receiver').prefetch_related('replies')
    return render(request, 'chats/conversation.html', {'messages': messages})
