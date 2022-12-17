#import required modules
#config module for providing keys
import config
#from bs4 import BeautifulSoup
import requests



#declare api key 
api_key = config.API_KEY
#print(key)
#print(base_url)


print("Welcome into the Weather app")
print("please search for a country ")



 
def location_input():
   
    city = input('Enter the name of the city.. >  ')
    res = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no")
    print ("Searching..\n")
    print(res.json())
    
    
location_input()


"""













"""

