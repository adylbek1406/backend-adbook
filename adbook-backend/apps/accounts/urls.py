from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


app_name = 'accounts'

urlpatterns = [
    # Auth
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # OTP
#    path('otp/send/', views.SendOTPView.as_view(), name='send_otp'),
#    path('otp/verify/', views.VerifyOTPView.as_view(), name='verify_otp'),
    
    # Profiles
    path('profiles/', views.ProfileListView.as_view(), name='profile_list'),
    path('profiles/me/', views.ProfileDetailView.as_view(), name='profile_me'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    
    # Followers
    path('profiles/<int:pk>/followers/', views.FollowersListView.as_view(), name='followers_list'),
    path('profiles/<int:pk>/following/', views.FollowersListView.as_view(), name='following_list'),
    path('profiles/<int:pk>/follow/', views.follow_view, name='follow'),
    
    # Devices
#    path('devices/', views.DeviceListView.as_view(), name='device_list'),
]

