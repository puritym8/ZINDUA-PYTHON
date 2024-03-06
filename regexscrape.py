import requests
import re
from bs4 import BeautifulSoup

url = "https://consolidatedbank.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#print(soup)

url_pattern = 