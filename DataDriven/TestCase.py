import openpyxl
import json
import requests
from DataDriven import Library

def test_Add_multiple_students():
    # API
    API_url = "http://thetestingworldapi.com/api/studentsDetails"

    # Parsing the Json from Extenal file
    file = open("C:/Users/Sunil.more/Desktop/PythonScrap/Add_Student.json", "r")
    Json_request = json.load(file)

    # Loading Excel and finding workbook, sheet and rows
    obj=Library.Comman("C:/Users/Sunil.more/Desktop/PythonScrap/data.xlsx", "Sheet1")
    col=obj.fetch_column_count()
    rows=obj.fetch_row_count()

    KeyList=obj.fetch_Key_names()

    for i in range(2, rows + 1):
        updated_json_req=obj.update_request_with_data(i, Json_request,KeyList )
        response= requests.post(API_url, updated_json_req)
        print(response.text)