import requests
from bs4 import BeautifulSoup



url = 'https://www.nehruplacemarket.com/price-list/ram-price-list.html?pagenum=1'
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

#print(soup.title.text)

results = soup.find(id="content")

#print(results.prettify())

table_rows = results.find_all('tr')

for row in table_rows:
    print(row.text,end="\n")
