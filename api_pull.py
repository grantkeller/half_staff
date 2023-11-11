import requests
import pandas as pd
import json

print("Enter your state to view it's flag status:")
user = input()

url = "https://flag-status.p.rapidapi.com/events/IN"

headers = {
	"X-RapidAPI-Key": "5564b17028msh775b564349f8e3cp120056jsn30bb2f54a949",
	"X-RapidAPI-Host": "flag-status.p.rapidapi.com"
}

response = requests.get(url, headers=headers).json()

with open("flag-status.json", 'w') as json_file:
    json.dump(response, json_file, indent=2)  

df = pd.DataFrame(response)

print(df)