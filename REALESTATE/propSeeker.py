import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import csv
import ast
import os
from urllib.request import Request, urlopen


#data arrays.
arr = []
prices = []

# use readline() to read the first line.
f = open('renturl.txt')
line = f.readline()

#While file is not empty, keep reading lines,appending to arr.
while line:
    arr.append(line)
    line = f.readline()
    f.close()
#If data.csv DNE create one, else append new stocks.
if(os.path.exists('rentaldata.csv') == True):
    f = csv.writer(open("rentaldata.csv","a"))
else:
    f = csv.writer(open("rentaldata.csv","w"))
    f.writerow(["ADDRESS","PRICE","YR_BLT"])

# For ignoring SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#input from user
#for i in range(len(arr)):
#    r = requests.get(arr[i])


url = arr[0]

# Making the website believe that you are accessing it using a mozilla browser

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.

soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')



property_json = {}
property_json['Details_Broad'] = {}
property_json['Address'] = {}

# Extract Title of the property listing


for title in soup.findAll('title'):
    print(title)
    property_json['Title'] = title.text.strip()
    break


#for meta in soup.findAll('meta', attrs={'name': 'description'}):
#    property_json['Detail_Short'] = meta['content'].strip()
#
#for div in soup.findAll('div', attrs={'class': 'character-count-truncated'}):
#    property_json['Details_Broad']['Description'] = div.text.strip()
#
#for (i, script) in enumerate(soup.findAll('script',attrs={'type': 'application/ld+json'})):
#




