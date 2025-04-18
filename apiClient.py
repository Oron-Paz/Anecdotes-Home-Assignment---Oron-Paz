import requests
import json

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        self.accessToken = None
    
    def authenticate(self, endpoint, credentials):
        #login
        response = requests.post(
            f"{self.base_url}/{endpoint}", 
            json=credentials
        )
        
        #get user access token 
        if response.status_code == 200:
            auth_data = response.json()
            if "accessToken" in auth_data:
                self.accessToken = auth_data["accessToken"]
                self.headers["Authorization"] = f"Bearer {self.accessToken}"
            return auth_data
        else:
            self.handle_error(response)
            return None
    
    # typical http get with endpoint and optinal params
    def get(self, endpoint, params=None):
        response = requests.get(
            f"{self.base_url}/{endpoint}",
            headers=self.headers,
            params=params
        )
        return self.process_response(response)
    
    #more abstracting
    def process_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            return self.handle_error(response)
    
    def handle_error(self, response):
        print(f"API Error: Status code {response.status_code}")
        print(f"Response: {response.text}")
        return None

#saves the evidence into json files
def save_evidence(evidence, output_dir="."):
    for evidence_id, data in evidence.items():
        with open(f"{output_dir}/{evidence_id}.json", "w") as f:
            json.dump(data, f, indent=2)
    
    print(f"Evidence saved to {output_dir}")