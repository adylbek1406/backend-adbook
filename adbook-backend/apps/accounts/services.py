from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from phonenumbers import parse
import pyotp
from apps.accounts.models import User, Profile, Device, OTP, LoginHistory
from core.exceptions import DeviceNotRecognized


User = get_user_model()


class AccountService:
    @staticmethod
    def create_user(email, password, username, **extra_fields):
        """Create user + profile"""
        user = User.objects.create_user(email=email, password=password, username=username, **extra_fields)
        Profile.objects.get_or_create(user=user)
        return user
    
    @staticmethod
    def generate_otp(otp_type, user):
        """Generate time-based OTP"""
        secret = pyotp.random_base32()
        totp = pyotp.TOTP(secret)
        code = totp.now()
        
        expires_at = timezone.now() + timedelta(minutes=10)
        
        otp = OTP.objects.create(
            user=user,
            otp_type=otp_type,
            code=code,
            expires_at=expires_at
        )
        return code, secret
    
    @staticmethod
    def verify_otp(user, otp_type, code):
        """Verify OTP code"""
        try:
            otp = OTP.objects.filter(
                user=user, 
                otp_type=otp_type,
                is_used=False
            ).latest('created_at')
            
            if otp.is_expired() or otp.code != code:
                otp.attempts += 1
                otp.save()
                return False
                
            otp.is_used = True
            otp.save()
            return True
        except OTP.DoesNotExist:
            return False
    
    @staticmethod
    def register_device(user, device_id, device_type, name, ip_address):
        """Register/activate device"""
        device, created = Device.objects.get_or_create(
            user=user,
            device_id=device_id,
            defaults={'device_type': device_type, 'name': name}
        )
        
        if created:
            LoginHistory.objects.create(
                user=user,
                device=device,
                ip_address=ip_address,
                is_successful=True
            )
        
        device.is_active = True
        device.save()
        return device
    
    @staticmethod
    def validate_device(user, device_id, ip_address):
        """Check if device is registered"""
        try:
            device = Device.objects.get(user=user, device_id=device_id, is_active=True)
            LoginHistory.objects.create(
                user=user,
                device=device,
                ip_address=ip_address,
                is_successful=True
            )
            return True
        except Device.DoesNotExist:
            raise DeviceNotRecognized()

