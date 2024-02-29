import requests
from bs4 import BeautifulSoup

url = "https://www.consolidated-bank.com"

response = requests.get(url)


#print (response.status_code)

#print(response.content)

soup = BeautifulSoup(response.content, "html.parser")

#print (soup)

paragraph = soup.find_all("p")

print(paragraph)




