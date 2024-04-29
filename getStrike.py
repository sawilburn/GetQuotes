import requests

url = "https://api.marketdata.app/v1/options/strikes/AAPL/?date=2024-03-05&expiration=2024-06-21"

response = requests.request("GET", url)

print(response.text)


