import pytest
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from apps.accounts.models import User, Profile


User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(
        email='test@example.com',
        username='testuser',
        password='testpass123'
    )


class TestAuthViews(APITestCase):
    
    def test_register_success(self):
        url = reverse('accounts:register')
        data = {
            'email': 'newuser@example.com',
            'username': 'newuser',
            'password': 'securepass123'
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(email='newuser@example.com').exists()
    
    def test_login_success(self, user):
        url = reverse('accounts:login')
        data = {
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
    
    def test_profile_detail(self, user):
        profile = Profile.objects.get(user=user)
        url = reverse('accounts:profile_me')
        self.client.force_authenticate(user=user)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['followers_count'] == 0

