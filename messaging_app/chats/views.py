# chats/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

User = get_user_model()


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Create a conversation with current user as a participant
        conversation = serializer.save()
        conversation.participants.add(self.request.user)
        conversation.save()

    def get_queryset(self):
        # Only return conversations where the current user is a participant
        return self.queryset.filter(participants=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the sender to the current user
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        # Only return messages where the user is a participant in the conversation
        return self.queryset.filter(conversation__participants=self.request.user)
