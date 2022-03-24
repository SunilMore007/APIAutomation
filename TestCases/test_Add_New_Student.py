import requests
import json

# command to execute: pytest -v -s  .\test_Add_New_Student.py

def test_add_student_data():
    API_url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/Sunil.more/Desktop/PythonScrap/Add_Student.json", "r")
    Json_request = json.load(file)
    response = requests.post(API_url, Json_request)
    print(response.text)


def test_get_student_data():
    API_url = "http://thetestingworldapi.com/api/studentsDetails/1106473"
    response = requests.get(API_url)
    print(response.text)
    json_response = response.json()
    print(json_response)
    data_dict = json_response["data"]
    print(data_dict["id"])
    assert data_dict["id"] == 1106473


def test_Update_student_data():
    API_url = "http://thetestingworldapi.com/api/studentsDetails/1106473"
    file = open("C:/Users/Sunil.more/Desktop/PythonScrap/Update_Student.json", "r")
    json_request = json.load(file)
    response = requests.put(API_url, json_request)
    print(response.text)


def test_get_updated_student_data():
    API_url = "http://thetestingworldapi.com/api/studentsDetails/1106473"
    response = requests.get(API_url)
    print(response.text)


def test_delete_student_data():
    API_url = "http://thetestingworldapi.com/api/studentsDetails/1106473"
    response = requests.delete(API_url)
    print(response.text)


def test_get_deleted_student_data():
    API_url = "http://thetestingworldapi.com/api/studentsDetails/1106473"
    response = requests.get(API_url)
    print(response.text)
