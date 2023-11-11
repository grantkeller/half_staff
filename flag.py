import requests
import pandas as pd

print("Enter your state to view it's flag status:\n")
user = input()

url = "https://flag-status.p.rapidapi.com/events/{user}".format(user)

headers = {
	"X-RapidAPI-Key": "5564b17028msh775b564349f8e3cp120056jsn30bb2f54a949",
	"X-RapidAPI-Host": "flag-status.p.rapidapi.com"
}

response = requests.get(url, headers=headers).json()

with open('flag-{user}.json'.format(user), 'w') as f:
    f.write(response, f)

df = pd.DataFrame(response)

print(df)