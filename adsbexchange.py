import requests

url = "https://adsbexchange-com1.p.rapidapi.com/json/lat/51.46888/lon/-0.45536/dist/50/"

headers = {
    'x-rapidapi-key': "1815e86cc7msh82af6ef8e7274f3p1f9d06jsn039e5c976071",
    'x-rapidapi-host': "adsbexchange-com1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
