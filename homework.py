import json
import requests
from jsonschema import validate
from schemas import post_users, put_update, post_create


url1 = "https://reqres.in"
key = {'x-api-key': 'reqres-free-v1'}
#1. на каждый из методов GET/POST/PUT/DELETE ручек reqres.in
#2. Позитивные/Негативные тесты на одну из ручек.
#3. На разные статус-коды 200/201/204/404/400

def test_update_200status_put_positive():
    response = requests.request("PUT", url=f"{url1}/api/users/2", headers=key, params={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200
#    validate(response.json(), schema=put_update)


def test_create_201status_post_positive():
    response = requests.request("POST", url=f'{url1}/api/users', headers=key, data={"name": "morpheus", "job": "leader"})
    assert response.status_code == 201
#    validate(response.json(), schema=post_create)


def test_get_users_204status_delete_positive():
    response = requests.delete(url=f'{url1}/api/users/2', headers=key )
    assert response.status_code == 204
#    response.json() is None


def test_login_unsuccessful_400status_post_negative():
    response = requests.post(url=f'{url1}/api/login', headers=key, json={"email": "peter@klaven"})
    assert response.status_code == 400
    response.json() == {"error": "Missing password"}


def test_single_user_not_found_404status_get_negative():
    response = requests.get(url="https://reqres.in/api/users/23", headers=key)
    assert response.status_code == 404
    response.json() == {}
