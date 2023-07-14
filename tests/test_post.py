import requests
import pytest
from utilities.ReadConfiguration import *
from utilities.random_user import Random_user

@pytest.mark.usefixtures("create_and_delete_user", "random_data")
class TestPost:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.user = self.user
        self.data = Random_user()

    def test_successful_create_user_post_code_201(self):
        url = f'{get_base_url()}/users/{self.user["id"]}/posts'
        headers = get_headers()
        post = {"title": self.data.random_title, "body": self.data.random_body}
        response = requests.post(url=url, headers=headers, json=post)
        assert response.status_code == 201

    def test_successful_create_user_post_contains_title(self):
        url = f'{get_base_url()}/users/{self.user["id"]}/posts'
        headers = get_headers()
        post = {"title": self.data.random_title, "body": self.data.random_body}
        response = requests.post(url=url, headers=headers, json=post)
        assert response.json()["title"] in self.data.random_title

    def test_with_incorrect_user_id(self):
        url = f'{get_base_url()}/users/{000000000000}/posts'
        headers = get_headers()
        post = {"title": self.data.random_title, "body": self.data.random_body}
        response = requests.post(url=url, headers=headers, json=post)
        assert response.status_code == 422

    def test_with_incorrect_headers(self):
        url = f'{get_base_url()}/users/{self.user["id"]}/posts'
        headers = ""
        post = {"title": self.data.random_title, "body": self.data.random_body}
        response = requests.post(url=url, headers=headers, json=post)
        assert response.status_code == 401
        assert response.json()["message"] in "Authentication failed"













