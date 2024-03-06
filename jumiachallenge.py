import requests
import csv
from bs4 import BeautifulSoup


url = "https://www.jumia.co.ke/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

#print (soup)

#product name
headings = soup.find_all("prdname")

print(headings)

