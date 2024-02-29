import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.nytimes.com/"

response = requests.get(url)
#to get the status_code
#print(response)

#print = (response.content)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

#article titles
headings = soup.find_all("h1")

#print(headings)

#article descriptions
descrptions = soup.find_all("p")
#print(descrptions)

#with open("info.csv", "w") as file:
    #for heading in headings:
        #print(heading.text)

with open("info.csv", "w") as file:
    writer = csv.writer(file)
    for heading in headings:
        writer.writerow(heading)
        

