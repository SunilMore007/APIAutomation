import json
import requests
import jsonpath
import pytest

# API URL
url = "https://reqres.in/api/users?page=2"


@pytest.mark.Regression
def test_fetch_user_details():
    # Send Get Request
    response = requests.get(url)

    # Fetch response  Headers
    print(response.headers.get("Date"))

    # validate Status code
    print(response.status_code)  # Status code =200
    assert response.status_code == 200

    response_dict = json.loads(response.text)
    print(response_dict['page'])
    # print(response_dict['data'][0])
    print(response_dict['data'][0]['email'])
