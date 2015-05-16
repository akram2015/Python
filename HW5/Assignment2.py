# this program will let user enter country code and will output back the country name for the provided code and the capital of the country.

import urllib.request
import json
from pprint import pprint

#while True:  # if we want to keep asking user to enter new code

try :
    country_code = input("Enter a country code to get (country name and capital): ")
    page = urllib.request.urlopen("https://restcountries.eu/rest/v1/alpha/" + country_code) # URL + country code
    content = page.read()
    content_string = content.decode("utf-8") # convert source code from byte to sting
         
    json_data = json.loads(content_string)  # encode data to json
        
    print(json_data["name"])     # print the name of the country
    print(json_data["capital"])  # print the capital of the country
        
except :
    print("The code does not found!")
    
                
    
    

