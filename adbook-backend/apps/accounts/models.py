from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
# from phonenumber_field.modelfields import PhoneNumberField
import pyotp

from core.models import TimeStampedModel, SoftDeleteModel


class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='adbook_users',
        blank=True,
        related_query_name='adbook_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='adbook_users',
        blank=True,
        related_query_name='adbook_user',
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['phone']),
            GinIndex(fields=['email']),  # For search
        ]

    def send_email_verification(self):
        otp = pyotp.random_base32()[:6]
        # Store OTP in Redis (TTL 5min)
        # send_mail(...)

    def verify_email(self, otp):
        pass  # Redis check

    def __str__(self):
        return self.email


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='profiles/', blank=True)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    is_private = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
        ]


class Device(TimeStampedModel, SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    device_id = models.CharField(max_length=255, unique=True)
    platform = models.CharField(max_length=50)  # ios/android/web
    last_ip = models.GenericIPAddressField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'is_active']),
            models.Index(fields=['device_id']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['user', 'device_id'], name='unique_user_device')
        ]


class LoginHistory(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    is_successful = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'created_at']),
        ]


class OTP(TimeStampedModel, SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    otp_code = models.CharField(max_length=6)
    otp_type = models.CharField(max_length=20, choices=[('email', 'Email'), ('phone', 'Phone'), ('login', 'Login')])
    is_used = models.BooleanField(default=False)
    expiry_time = models.DateTimeField()

    class Meta:
        indexes = [
            models.Index(fields=['user', 'otp_type', 'is_used']),
        ]

    def is_expired(self):
        return timezone.now() > self.expiry_time
