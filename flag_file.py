import pandas as pd
import json
from datetime import datetime

json_file_path = 'flag-status.json'
current_date_time = datetime.now()
current_date = str(current_date_time.date())

# df = pd.read_json(json_file_path)

# last_record = df[['date_start', 'date_end']].tail(1)

# print(current_date)
# print(df[['date_start', 'date_end']])

with open('flag-status.json', 'r') as file:
    data = json.load(file)

last_record = data[-1]
date_start = last_record['date_start']
date_end = last_record['date_end']

if current_date == date_start or date_end:
    print('1')
else:
    print('0')