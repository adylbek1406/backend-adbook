from apps.accounts.models import User, Profile, LoginHistory
from django.db.models import Q


class UserSelector:
    @staticmethod
    def get_active_users():
        """Get recently active users"""
        from django.utils import timezone
        thirty_days_ago = timezone.now() - timedelta(days=30)
        return User.objects.filter(
            is_active=True,
            last_login__gte=thirty_days_ago
        ).select_related('profile')
    
    @staticmethod
    def get_user_profile(user_id):
        """Get user with profile"""
        return User.objects.filter(id=user_id).select_related('profile').first()
    
    @staticmethod
    def search_users(query):
        """Full-text user search"""
        return User.objects.filter(
            Q(email__icontains=query) | Q(username__icontains=query)
        ).select_related('profile')[:20]
    
    @staticmethod
    def get_user_devices(user_id):
        """Get user's active devices"""
        return Device.objects.filter(
            user_id=user_id,
            is_active=True
        ).order_by('-last_seen')
    
    @staticmethod
    def get_login_history(user_id, limit=50):
        """Recent login history"""
        return LoginHistory.objects.filter(
            user_id=user_id,
            is_successful=True
        ).select_related('device').order_by('-login_time')[:limit]

