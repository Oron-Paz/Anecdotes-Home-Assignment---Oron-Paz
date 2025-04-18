import requests
import json

response = requests.get("https://dummyjson.com/test")
print (response.json())

username = "emilys"
password = "emilyspass"

def connectivity_test(username: str, password: str):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post('https://dummyjson.com/auth/login', json = payload)
    if response.status_code == 200:
        data = response.json()
        print("Response data:", data)
        return data
    else:
        print(f"Login error with code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

valid_login = connectivity_test("emilys", "emilyspass")
invalid_login = connectivity_test("wrong", "wrong")