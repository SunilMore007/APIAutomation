import requests
import json


def test_oauth_api():
    Token_url = "http://thetestingworldapi.com/Token"
    data = {'grant_type': 'password', 'username': 'admin', 'password': 'adminpass'}
    response = requests.post(Token_url, data)
    print(response.text)
    json_response = response.json()
    token_value = json_response["access_token"]
    print(token_value)

    auth = {'Authorization': 'bearer' + token_value}

    API_URL = "http://thetestingworldapi.com/api/StDetails/1104"
    response = requests.get(API_URL, headers=auth)
    print(response.text)
