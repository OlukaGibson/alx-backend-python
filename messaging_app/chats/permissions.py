from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allow only participants of a conversation to access its messages
    """

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "participants"):  # Conversation
            return request.user in obj.participants.all()
        if hasattr(obj, "conversation"):  # Message
            return request.user in obj.conversation.participants.all()
        return False
