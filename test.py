import requests

url = "https://api.thedogapi.com/v1/images/search?mime_types=jpg"

req = requests.get(url).json()
print(req)
print(type(req))
print(req[0]['url'])

url = "https://api.thedogapi.com/v1/images/search?mime_types=jpg"
req = requests.get(url).json()
print(req[0]['url'])