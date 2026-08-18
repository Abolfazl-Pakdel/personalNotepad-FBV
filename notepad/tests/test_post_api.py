

from rest_framework.test import APIClient
import pytest
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(username="admin", password="123")
    return user


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self, api_client):
        url = reverse("notepad:api-v1:note-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("notepad:api-v1:note-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user
        # api_client.force_login(user=user)
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_400_status(self, api_client, common_user):
        url = reverse("notepad:api-v1:note-list")
        data = {
            "content": "description",
            "is_pinned": False,
        }
        user = common_user
        # api_client.force_login(user=user)
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400