import requests
import json

response = requests.get("https://dummyjson.com/test")
print (response.json())