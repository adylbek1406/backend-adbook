from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from apps.accounts.models import Profile
from apps.accounts.serializers import (
    RegisterSerializer, LoginSerializer, ProfileSerializer, UserSerializer
)
from apps.accounts.services import AccountService
from apps.accounts.permissions import IsProfileOwner
from apps.accounts.selectors import UserSelector


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(
        responses={201: UserSerializer},
        description="Register new user (email + auto-profile)"
    )
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(responses={200: 'tokens'})
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })


class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"})
        except Exception:
            return Response({"message": "Refresh token not found"}, status=400)


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.select_related('user')


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwner]
    
    def get_object(self):
        user = self.request.user if self.request.user.is_authenticated else None
        if self.kwargs.get('pk') == 'me' or not user:
            profile = self.request.user.profile
        else:
            profile = Profile.objects.select_related('user').get(user_id=self.kwargs['pk'])
        return profile


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_view(request, pk):
    profile = Profile.objects.get(user_id=pk)
    # Follow logic using service layer
    return Response({'status': 'followed'})


class FollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        profile = Profile.objects.get(user_id=self.kwargs['pk'])
        return profile.user.followers.all()

