from faker import Faker
import requests


# url = "https://gorest.co.in/public/v2/users?gender=male&status=active"
url = "https://gorest.co.in/public/v2/users.xml"

# params={'gender': 'male', 'status': 'active'}
params=[('gender', 'male'), ('status','active')]
headers = {"Accept":"application/json",
           "Content-Type":"application/json",
           "Authorization": "Bearer 4084f7dc0be9da3acbbd45633a658b0122cc9db471f0b4a75abc245a8937ad76"}

response = requests.get(url=url, headers=headers, params=params)
print(response)
# print(response.status_code)
print(response.text)
# print(len(response.json()))

url = "https://gorest.co.in/public/v2/users/3357114"

headers = {"Accept":"application/json",
           "Content-Type":"application/json",
           "Authorization": "Bearer 4084f7dc0be9da3acbbd45633a658b0122cc9db471f0b4a75abc245a8937ad76"}

response = requests.get(url=url, headers=headers)
print(response.status_code)
print(response.json())
print(len(response.json()))


url = "https://gorest.co.in/public/v2/users/3359320"

headers = {"Accept":"application/json",
           "Content-Type":"application/json",
           "Authorization": "Bearer 4084f7dc0be9da3acbbd45633a658b0122cc9db471f0b4a75abc245a8937ad76"}

response = requests.delete(url=url, headers=headers)
print(response.status_code)
print(response.json())
print(len(response.json()))

url = "https://gorest.co.in/public/v2/users"

headers = {"Accept":"application/json",
           "Content-Type":"application/json",
           "Authorization": "Bearer 4084f7dc0be9da3acbbd45633a658b0122cc9db471f0b4a75abc245a8937ad76"}

user = {"name": "Alex Rjdgufvddnjfndk", "email": "qdjijdbbjdofdfeowertd526264@gmail.com", "gender": "male", "status": "inactive"}
response = requests.post(url=url, headers=headers, json=user)
print(response.status_code)
print(response.headers)
print("-----JSON----------------")
print(response.json())
res = response.json()["id"]
print(res)


