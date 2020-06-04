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
import time


#TODO - do recon (url files) comparison to count days on url
#TODO - for loop to handle/do multiple URLs
#TODO - write to CSV


#data arrays.
houses = []
recon_houses = []
prices = []
house_data = []
rawdata = []
finaldata = []
# use readline() to read the first line.
with open('buyurl.txt') as urls:
    house_url = urls.read().splitlines()
    for line in house_url:
        houses.append(line)
urls.close()


with open('buyrecon.txt') as urls:
    house_url_recon = urls.read().splitlines()
    for line in house_url_recon:
        print(line)
        recon_houses.append(line)
urls.close() 

result = list(set(houses) - set(recon_houses))
print(result)

if not result:
    print("no URL's added since last run")
else:
    f = csv.writer(open("buyrecon.txt","a",newline=''))
    
    for i in range(len(result)):
time.sleep(100)

if houses not in recon_houses:
    print(recon_houses)

#If data.csv DNE create one, else append new stocks. make this a module
if(os.path.exists('buydata.csv') == True):
    f = csv.writer(open("buydata.csv","a"))
else:
    f = csv.writer(open("buydata.csv","w"))
    f.writerow(["SALE_STS","PRICE_AMT","FULL_ADDRESS","ADDRESS","CITY","STATE_CD","ZIP_CD","BEDS","BATH","TYPE","YR_BUILT","HEATING","COOLING","PARKING","HOA","LOT","PRICE_SQFT","DESC_SHRT","DESC_LNG","URL","IMAGE","TIME_ZILLOW","VIEWS","SAVES","TIME_URL"])

# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = houses[0]

# Making the website believe that you are accessing it using a mozilla browser
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.
#soup = BeautifulSoup(webpage, 'html.parser')
soup = BeautifulSoup(webpage, 'lxml')
html = soup.prettify('utf-8')





test = soup.findAll('span')
market_status = test[97].text

# Extraction of DATA
market_status = (soup.find('span', {'class' : 'sc-bGbJRg fFPekb ds-status-details'}))
metaData = (soup.findAll('meta'))
facts = soup.findAll('span', attrs={'class': 'ds-body ds-home-fact-value'})
views = (soup.find('div', {'class' : 'sc-gVLVqr ftFSjV'}))

print(views)
# Cleaning up market status and setting boolean, appending to final data list
if market_status.text == "For sale":
    market_status = "y"
else:
    market_status = "n"
finaldata.append(market_status)

print(market_status)

# cleaning up Price data 
finaldata.append(float(metaData[31].get('content')))


# cleaning up address data 
address = metaData[28].get('content').split('|')
finaldata.append(' '.join(address[0].split()))
address = address[0].split(',')
finaldata.append(' '.join(address[0].split()))
finaldata.append(' '.join(address[1].split()))
address = address[2].split()
finaldata.append(address[0])
finaldata.append(address[1])

# cleaning up stats data 
temp_data = []
data_vals = [24,25,1,26,29,27]
num_elems = len(metaData)
for i in range(num_elems):
    if i in data_vals:
        temp_data.append(metaData[i].get('content'))

idx = [1,2,0,3,5,4]
finaldata.append(int(temp_data[1]))
finaldata.append(int(temp_data[2]))

# cleaning up facts data 
temp_facts = []
num_elems = len(facts)
for i in range(num_elems):
    temp_facts.append(facts[i].text)

finaldata.append(temp_facts[0])
finaldata.append(int(temp_facts[1]))
finaldata.append(temp_facts[2])
finaldata.append(temp_facts[3])
finaldata.append(temp_facts[4])

HOA = (re.findall(r'\d+',temp_facts[5]))
SQFT = temp_facts[6].replace(',','')
SQFT = (re.findall(r'\d+',SQFT))
SQFT_PR = (re.findall(r'\d+',temp_facts[7]))

finaldata.append(int(HOA[0]))
finaldata.append(int(SQFT[0]))
finaldata.append(int(SQFT_PR[0]))


idx = [1,2,0,3,5,4]
finaldata.append(temp_data[0])
finaldata.append(temp_data[5])
finaldata.append(temp_data[4])


#print(repr(address[0]))
stats = views.text
stats = stats.replace(',','')
stats_final = []
final_stats = re.findall(r'\d+',stats)
num_elems = len(final_stats)
for i in range(num_elems):
    finaldata.append(int(final_stats[i]))

print(finaldata)

f = csv.writer(open("buydata.csv","a"))
f.writerow(finaldata)

#DATA CLEANUP 
#splitting = str(rawdata)
#data = splitting.split('"')
#price = float(data[1])
#print(price - 180000)


property_json = {}
property_json['Details_Broad'] = {}
property_json['Address'] = {}
#print(repr(x))


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
    
#with open('data.json', 'w') as outfile:
#    json.dump(property_json, outfile, indent=4)
#    
#with open('output_file.html', 'wb') as file:
#    file.write(html)

print ('----------Extraction of data is complete. Check json file.----------')

