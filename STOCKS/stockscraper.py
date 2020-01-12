import bs4
import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
import os 
import os.path
from datetime import date

#data arrays.
arr = []
prices = []

# use readline() to read the first line.
f = open('stockurl.txt')
line = f.readline()

#While file is not empty, keep reading lines,appending to arr.
while line:
    arr.append(line)
    line = f.readline()
f.close()

#If data.csv DNE create one, else append new stocks.
if(os.path.exists('stockdata.csv') == True):
    f = csv.writer(open("stockdata.csv","a"))
else:
    f = csv.writer(open("stockdata.csv","w"))
    f.writerow(["STOCK_NAME","PRICE","DATE"])

#Request webpage to extract stock data and write to csv file.
for i in range(len(arr)):
    r = requests.get(arr[i])
    soup=bs4.BeautifulSoup(r.text,'lxml')
    price = soup.find_all('div',{"id":"quote-header-info"})[0].find_all('span')[1].text
    price = price.replace(",","")
    name = soup.find_all('div',{"id":"quote-header-info"})[0].find_all('h1')[0].text
    name = name.partition(' ')[0]
    f.writerow([name,price,date.today()])

#os.system('./copy.sh')
