#!/usr/bin/python

import requests, bs4

result = requests.get('https://forecast.weather.gov/MapClick.php?lat=43.61284000000006&lon=-116.39174999999994')
result.raise_for_status()

weather = bs4.BeautifulSoup(result.text, 'html.parser')
temperature = weather.select('#current_conditions-summary')
details = weather.select('#current_conditions_detail')
#print(elements[0].getText())
for element in temperature:
    print(element.getText())

# the elements list contains all matches
for element in details:
    print(element.getText())
