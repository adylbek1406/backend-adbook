from django.db import models
from apps.accounts.models import User
from django.contrib.postgres.indexes import GinIndex


class ChatRoom(models.Model):
    ROOM_TYPES = [
        ('direct', 'Direct Message'),
        ('group', 'Group Chat'),
    ]
    
    name = models.CharField(max_length=255, blank=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, default='direct')
    max_members = models.PositiveSmallIntegerField(default=2)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['is_active']),
        ]


class ChatRoomMember(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_rooms')
    joined_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    last_seen = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['room', 'user']),
            models.Index(fields=['user']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['room', 'user'], name='unique_room_member')
        ]


class Message(models.Model):
    MESSAGE_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('file', 'File'),
    ]
    
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES, default='text')
    attachment = models.FileField(upload_to='chat/attachments/', blank=True, null=True)
    
    is_deleted = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['room', 'created_at']),
            models.Index(fields=['author']),
        ]
        ordering = ['created_at']


class MessageRead(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='reads')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['message']),
            models.Index(fields=['user']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['message', 'user'], name='unique_message_read')
        ]

