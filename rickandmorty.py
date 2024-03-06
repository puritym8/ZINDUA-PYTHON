import requests
import re
from bs4 import BeautifulSoup
import csv

url = ("https://rickandmortyapi.com")

#to get the status code
response = requests.get(url)
#print(response)

#print = (response.content)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

parameters = {"pages": 3}
response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()
    characters = data["results"][:20]  # Fetching the first 20 characters
    for character in characters:
        print(character["name"])

