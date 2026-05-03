import requests
from bs4 import BeautifulSoup



url = 'https://www.nehruplacemarket.com/price-list/ram-price-list.html?pagenum=1'
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

#print(soup.title.text)

results = soup.find(id="content")

#print(results.prettify())

table_rows = results.find_all('tr')

#for row in table_rows:
    ##print(row.text,end="\n")

data_records = []
iterator = 1
list_of_records = []
row_records = []
for row in table_rows:

    for column in row:
        data_records.append(column.text)
        row_records.append(column.text)
        iterator +=1
        #print(row_records)
        if iterator == 5:
            list_of_records.append(row_records)
            row_records = []
            iterator=1
            #print(row_records)
#print(data_records)
row_titles = data_records[4:9]
#print(row_titles)
print(list_of_records)
#print(list_of_records)
#print(data_records[4:])

"""currently the data doesnt look the way I want import 
    I think what I will do is have an empty list in for every row in table_rows
    then ill append every column to that empty row list
    then ill append the row list to the data_records
    however I must come up with a way of appending the row to the data_records and deleting the contents of the row after 5 increments
    however since the top few rows have titles I must first clean the table that is received then do all the operations to clean the data
    its possible that pandas could even be useful, think about this some more"""
