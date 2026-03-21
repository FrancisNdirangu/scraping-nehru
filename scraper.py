import requests

response = requests.get('https://www.nehruplacemarket.com/price-list/ram-price-list.html?pagenum=1')
print(response.status_code)

cont= response.content
tx = response.text
enc = response.encoding
js = response.json

print(js)