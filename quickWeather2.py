#! python3
# quickWeather2.py - Prints current weather for Boston and sends via text using Twilio (created method in textMyself.py)
from datetime import date
import textMyself, json, requests, sys, calendar

# Compute Date variables
today = date.today()
weekDay = calendar.day_name[today.weekday()]
date = date.today().strftime("%m/%d/%Y")

# Download the JSON data from api

# City ID, Boston: 4930956
url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=4930956&units=imperial&APPID=' # Add API key here
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a python variable

weatherData = json.loads(response.text)

# Print today's date
#print("Today is " + weekDay+ ", "+ date)

# Print weather descriptions

w = weatherData['list']

tmp = []

for i in w:
	if i['dt_txt'][:10] == today:
		if i['weather'][0]['main'] == 'Rain':
			tmp.append(i['dt_txt'][-8:-3] + ': ' + i['weather'][0]['main'] + ' - ' + i['weather'][0]['description'] \
			+ ' ' + str(i['clouds']['all']) + '%' + ' - ' + str(i['main']['temp']) + '°F' + '\n')
		elif i['weather'][0]['main'] == 'Clouds':
			tmp.append(i['dt_txt'][-8:-3] + ': ' + i['weather'][0]['main'] + ' - ' + i['weather'][0]['description'][:-7] \
			+ ' ' + str(i['clouds']['all']) + '%' + ' - ' + str(i['main']['temp']) + '°F' + '\n')

message = 'Current weather in Boston:\n' + "".join(tmp)
print(message)
textMyself.textmyself(message)
