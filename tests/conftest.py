import pytest
import requests

from utilities.random_user import Random_user
from utilities.ReadConfiguration import *

@pytest.fixture(autouse=True)
def create_and_delete_user(request, random_data):
    global user
    user = None
    url = f"{get_base_url()}/users"
    headers = get_headers()
    user = {"name": f"{random_data.first_name} {random_data.last_name}", "email": random_data.email, "gender": random_data.gender, "status": random_data.status}
    response = requests.post(url=url, headers=headers, json=user)
    print(f"Create user:\n{response.json()}")
    user = response.json()
    request.cls.user = user
    yield user
    delete = requests.delete(url=f"{url}/{user['id']}", headers=headers)
    print(f"Delete code: \n{delete.status_code}")

@pytest.fixture(autouse=True)
def random_data():
    return Random_user()