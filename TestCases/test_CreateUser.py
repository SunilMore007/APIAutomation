import json
import pytest
import jsonpath
import requests

# API URL
url = "https://reqres.in/api/users"


@pytest.fixture()
def start_execution():
    # Read input Json File
    global file
    file = open('C:\\Users\\Sunil.more\\Desktop\\PythonScrap\\createUser.json', 'r')


a = 1

@pytest.mark.smoke
@pytest.mark.skipif(a > 10, reason="Condition is not satisfied")
def test_create_new_user(start_execution):
    request_json = json.load(file)

    # Make POST request with Json Input Body
    response = requests.post(url, request_json)

    # validating response code
    print(response.status_code)
    assert response.status_code == 201

    # Parse response to Json Format
    JsonResponse = response.json()
    print(JsonResponse)

    # Pick ID using Json path
    print(JsonResponse['id'])

@pytest.mark.Sanity
def test_create_other_user(start_execution):
    # Read input Json File
    #file = open('C:\\Users\\Sunil.more\\Desktop\\PythonScrap\\createUser.json', 'r')
    request_json = json.load(file)
    response = requests.post(url, request_json)
    print(response.status_code)
    assert response.status_code == 201
    JsonResponse = response.json()
    print(JsonResponse)
    # Pick ID using Json path
    print(JsonResponse['id'])
