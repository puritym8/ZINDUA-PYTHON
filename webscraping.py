import requests

response = requests.get("https://www.consolidated-bank.com")

print (response.status_code)
