import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import csv
import ast
import os
import re
from urllib.request import Request, urlopen


#data arrays.
arr = []
prices = []
house_data = []
# use readline() to read the first line.
f = open('buyurl.txt')
line = f.readline()

#While file is not empty, keep reading lines,appending to arr.
while line:
    arr.append(line)
    line = f.readline()
    f.close()
#If data.csv DNE create one, else append new stocks.
if(os.path.exists('buydata.csv') == True):
    f = csv.writer(open("buydata.csv","a"))
else:
    f = csv.writer(open("buydata.csv","w"))
    f.writerow(["PRICE_AMT","ADDRESS","CITY","STATE_CD","ZIP_CD","BEDS","BATH","TYPE","YR_BUILT","HEATING","COOLING","PARKING","HOA","LOT","PRICE_SQFT","DESC_SHRT","DESC_LNG","URL","IMAGE"])

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

#soup = BeautifulSoup(webpage, 'html.parser')
soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')

property_json = {}
property_json['Details_Broad'] = {}
property_json['Address'] = {}

# Extract Title of the property listing

#x = soup.find('meta', attrs={'property': 'og:title'})
x = soup.findAll('meta', attrs={'name': 'description'})
print(soup.find('meta', attrs={'property': 'og:description'}))
print(soup.find('meta', attrs={'property': 'product:price:amount'}))
print(soup.findAll('meta', attrs={'property': 'zillow_fb:beds'}))
print(soup.findAll('meta', attrs={'property': 'zillow_fb:baths'}))
facts = soup.findAll('span', attrs={'class': 'ds-body ds-home-fact-value'})
print(soup.findAll('meta', attrs={'property': 'og:url'}))
print(soup.findAll('meta', attrs={'property': 'og:image'}))
print('\n\n\n')

i = 0
for i in range(len(facts)):
    print(facts[i].text)

print(x)
print("\n\n\n")
y = str(x[0]).replace("<meta content=\"","")
y = y.replace("\" name=\"description\"/>","")
print(y)
y = y.split(",")
print(repr(y[0]),y[1],y[2])
print(repr(y[0].strip()))

#for title in soup.findAll('title'):
#    property_json['Title'] = title.text.strip()
#    break
#
#for meta in soup.findAll('meta', attrs={'name': 'description'}):
#    property_json['Detail_Short'] = meta['content'].strip()
#
#for div in soup.findAll('div', attrs={'class': 'character-count-truncated'}):
#    property_json['Details_Broad']['Description'] = div.text.strip()
#
##print(soup.findAll('script',attrs={'type': 'application/ld+json'}))
#print("\n\n\n")
#
#script = str(soup.find('script',attrs={'type': 'application/ld+json'}))
#
#script_formed = re.sub('<script type="application/ld+json">','',script)
#
#print(script_formed)
#json_data = json.loads(script)

#print(json_data['numberOfRooms'])
#for (i, script) in enumerate(soup.findAll('script',attrs={'type': 'application/ld+json'})):
#    if i == 0:
#        json_data = json.loads(script.text)
#        property_json['Details_Broad']['Number of Rooms'] = json_data['numberOfRooms']
#        property_json['Details_Broad']['Floor Size (in sqft)'] = json_data['floorSize']['value']
#        property_json['Address']['Street'] = json_data['address']['streetAddress']
#        property_json['Address']['Locality'] = json_data['address']['addressLocality']
#        property_json['Address']['Region'] = json_data['address']['addressRegion']
#        property_json['Address']['Postal Code'] = json_data['address']['postalCode']
#    if i == 1:
#        json_data = json.loads(script.text)
#        property_json['Price in $'] = json_data['offers']['price']
#        property_json['Image'] = json_data['image']
#        break
    
with open('data.json', 'w') as outfile:
    json.dump(property_json, outfile, indent=4)
    
with open('output_file.html', 'wb') as file:
    file.write(html)

print ('----------Extraction of data is complete. Check json file.----------')

