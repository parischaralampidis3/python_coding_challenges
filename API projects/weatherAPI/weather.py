
import config
import json
import requests


api_key = config.API_KEY


print("Welcome into the Weather app")
print("please search for a country ")


def location_input():

    city = input('Enter the name of the city.. >  ')

    try:
        res = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no")
        print ("Searching..\n")
       
        parse_json = json.loads(res.text)
        weather_status = json.dumps(parse_json["current"]["condition"].get("text"))

        localtime = json.dumps(parse_json["location"].get("localtime"), indent=4)
        temprature = json.dumps(parse_json["current"].get("temp_c"), indent=4)
        
    
        print("Weather Status: " + weather_status)
        print("Localtime is " + localtime  + " and " +  " the temprature (celcius) is "  + temprature)
    except:
      print("Exception thrown. x does not exist.")

location_input()


