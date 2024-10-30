import os
from time import process_time, sleep
import requests

# getting actual time in Berlin
response = requests.get("https://timeapi.io/api/time/current/zone?timeZone=Europe%2FBerlin")
print(response.status_code)
#converting data into dictionary
actual_time = response.json()
print(actual_time['date'])
time_str = str(actual_time['hour'])+ ":" + str(actual_time['minute']) + ":" + str(actual_time['seconds'])
print(time_str)
print("Success")
sleep(3)
#here we set new time 
os.system("time " + time_str)
