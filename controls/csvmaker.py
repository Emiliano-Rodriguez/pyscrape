import csv

generate(url):
#If data.csv DNE create one, else append new stocks. make this a module
    if(os.path.exists('buydata.csv') == True):
        f = csv.writer(open("buydata.csv","a"))
    else:
        f = csv.writer(open("buydata.csv","w"))
        f.writerow(["PRICE_AMT","ADDRESS","CITY","STATE_CD","ZIP_CD","BEDS","BATH","TYPE","YR_BUILT","HEATING","COOLING","PARKING","HOA","LOT","PRICE_SQFT","DESC_SHRT","DESC_LNG","URL","IMAGE"])
