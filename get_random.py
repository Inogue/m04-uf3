#!/bin/python3

import requests
import sys

api_url = "https://randomuser.me/api" 

response = requests.get(api_url)
info = response.json()
user_name=info["results"][0]["name"]
user_location=info["results"][0]["location"]
user_picture=info["results"][0]["picture"]

print("Name: "+user_name["first"]+" "+user_name["last"])
print("Location: "+user_location["street"]["name"]+" "+str(user_location["street"]["number"])+", "+user_location["city"]+", "+user_location["country"])
print("Profile: "+user_picture["large"])
