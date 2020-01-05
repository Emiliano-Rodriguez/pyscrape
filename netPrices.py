import bs4
import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
import os 

f = open('stocks.txt')
# use readline() to read the first line
line = f.readline()
prices = []
arr = []
x = []
y = []

# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
while line:
    arr.append(line)
    line = f.readline()
f.close()
#classNm.append("D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)")
#classNm.append("My(6px) Pos(r) smartphone_Mt(6px)")
f = csv.writer(open("data.csv","a"))
f.writerow(["bitCoin","GeneralElec","Disney","Sundance"])

for i in range(len(arr)):
    r = requests.get(arr[i])
    soup=bs4.BeautifulSoup(r.text,'lxml')
    price = soup.find_all('div',{"id":"quote-header-info"})[0].find_all('span')[1].text
    price = price.replace(",","")
    prices.append(price)
    print(prices) 

f.writerow(prices)

#with open('data.csv','r') as csvfile:
#    plots = csv.reader(csvfile, delimiter=',')
#    next(plots,None)
#    for row in plots:
#        x.append(row[0])
#        price = row[1].replace(",","")
#        print(price)
#        y.append(float(price))
#                
#plt.bar(x,y, label='Loaded from file!')
#plt.xlabel('Company')
#plt.ylabel('Price')
#plt.title('Interesting Graph\nCheck it out')
#plt.legend()
#plt.savefig("figure")
##Copy/email graphs/files
##os.system('./copy.sh')
