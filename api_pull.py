import requests
import pandas as pd
import json

def api_pull(state):
	url = f"https://flag-status.p.rapidapi.com/events/{state}"

	headers = {
		"X-RapidAPI-Key": "5564b17028msh775b564349f8e3cp120056jsn30bb2f54a949",
		"X-RapidAPI-Host": "flag-status.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers).json()
	return response

def file_save(response):
    with open("flag-status.json", 'w') as json_file:
        json.dump(response, json_file, indent=2)