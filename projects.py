import time
import requests
from bs4 import BeautifulSoup
import pandas as pd 
#######################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##########################
#This is my first web scraping project. This project will allow me to understand
#the practice behind we scraping for data scientists. With this new tool I will 
#be able to extract data from almost anywhere on the internet, and produce reports.
######################$$$$$$$$$$$$$$$$$$$$$########################################
#print("Hello World! Today, we are going to do some heavy webscraping")
#time.sleep(1)
#usr_input = input ("What website would you like to webscrape today: ")
#time.sleep(1)
#print("Thinking...")
#time.sleep(1)
#print("Okay great, I will read "+ usr_input+" as html!")


# here, page is making a "request" to download the webpage with the given URL. Now we have a "snapshot" of that specific webpage
page = requests.get('https://emiliano-rodriguez.github.io/projects.html')

# soup, will take note that it we will be parsing the webpage as "html" so soup will understand what its reading
soup = BeautifulSoup(page.text, 'html.parser')

rows = soup.find_all('ul')
print(rows)

print("\n")

projects = []
desc = []

for row in rows:
    print(row.get_text())
    projects.append(row.get_text())
#    print(projects[row])

print(len(projects))

#pd.DataFrame({'Title':Title, 'URL':URL}).to_csv('google_searches.csv')

