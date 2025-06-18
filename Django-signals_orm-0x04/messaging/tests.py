from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class SignalTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='alice', password='test123')
        self.user2 = User.objects.create_user(username='bob', password='test123')

    def test_notification_created_on_message(self):
        msg = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello Bob!")
        self.assertEqual(Notification.objects.filter(user=self.user2, message=msg).count(), 1)
