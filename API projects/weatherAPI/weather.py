#import required modules
#config module for providing keys
import config
import requests
import json

#declare api key 
response = requests.get(api_key)
api_key = config.api_key
url = "http://api.weatherapi.com/v1/current.json?key=api_key&q=location_input&aqi=no" 



#print(response.url)
print("Welcome into the Weather app")
print("please search for a country ")


def location_input():
    location_input = input("> ")
    response = requests.get(url)
    response.json()
    print (location_input)
location_input()

