import json
import requests


def test_add_student_data():
    API_url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/Sunil.more/Desktop/PythonScrap/Add_Student.json", "r")
    Json_request = json.load(file)
    response = requests.post(API_url, Json_request)
    print(response.text)
    json_response = response.json()
    id = json_response["id"]
    print(id)

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open("C:/Users/Sunil.more/Desktop/PythonScrap/Tech_Details.json", "r")
    json_request = json.load(file)
    json_request['id'] = id
    json_request['st_id'] = id
    response = requests.post(tech_api_url, json_request)
    print(response.text)

    address_api_url = "http://thetestingworldapi.com/api/addresses"
    file1 = open("C:/Users/Sunil.more/Desktop/PythonScrap/Stud_Address.json", "r")
    json_request1 = json.load(file1)
    print(json_request1)
    json_request1['stId'] = id
    response = requests.post(address_api_url, json_request1)
    print(response.text)

    final_details_api_url = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id)
    response = requests.get(final_details_api_url)
    print(response.text)
