import requests
import json

#tested api connection dont need this
response = requests.get("https://dummyjson.com/test")
print (response.json())

username = "emilys"
password = "emilyspass"

def connectivity_test(username: str, password: str):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post('https://dummyjson.com/auth/login', json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Response data:", data)
        return data
    else:
        print(f"Login error with code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def collect_evidence(accessToken):
    headers = {
        "Authorization": accessToken,
        "Content-Type": "application/json"
    }

    def collect_E1_userDetails():
        response = requests.get('https://dummyjson.com/auth/me', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to collect user details: {response.status_code}")
            return None
        
    def collect_E2_posts():
        pass

    return collect_E1_userDetails()

valid_login = connectivity_test("emilys", "emilyspass")

E1 = collect_evidence(valid_login['accessToken'])
print(E1)


#dont need this anymore
#invalid_login = connectivity_test("wrong", "wrong")