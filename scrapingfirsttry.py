
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

# Select Browser
driver = webdriver.Chrome("C:/Users/Richard/Downloads/chromedriverwin32/chromedriver.exe") #, options=options)

import time

# Select Website URL
driver.get('https://icare.fairfaxcounty.gov/ffxcare/search/commonsearch.aspx?mode=address')

# Locate Search Bar
searchBar = driver.find_element_by_id('inpStreet')

# Send Text to Search Bar
searchBar.send_keys('Clark')

# Import Keys Function
from selenium.webdriver.common.keys import Keys

# Send ENTER Instructions
searchBar.send_keys(Keys.ENTER)

# Click on the First Result
firstField = driver.find_elements_by_class_name("SearchResults")
for x in range(len(firstField)):
    if firstField[x].is_displayed():
        driver.execute_script("arguments[0].click();", firstField[x]);
        break;
        time.sleep(1)
page_source1 = driver.page_source

# Import BeautifulSoup
from bs4 import BeautifulSoup

# Using html.parser
soup = BeautifulSoup(page_source1, 'html.parser')

# Finds the Data on First Page of First Result
sideHeading = soup.find_all('td', attrs={'class':'DataletSideHeading'})
data = soup.find_all('td', attrs={'class':'DataletData'})


# Lists the Data Found
record1 = sideHeading[0]
record2 = sideHeading[1]
record3 = sideHeading[4]
record4 = sideHeading[8]

info1 = data[0]
info2 = data[1]
info3 = data[4]
info4 = data[8]

# Click On Sales Link
driver.find_element_by_link_text("Sales").click()
page_source2 = driver.page_source

# Using html.parser
soup = BeautifulSoup(page_source2, 'html.parser')

# Finds the Data on Sale Link

topHeading = soup.find_all('td', attrs={'class':'DataletTopHeading'})
data2 = soup.find_all('td', attrs={'class':'DataletData'})

record5 = topHeading[0]
record6 = topHeading[1]
record7 = topHeading[2]
record8 = topHeading[3]

info5 = data2[0]
info6 = data2[1]
info7 = data2[2]
info8 = data2[3]
info9 = data2[4]
info10 = data2[5]
info11 = data2[6]
info12 = data2[7]

# Shows How I Want The Data to Look In The Table
krish = {record1.contents[0]:[info1.contents[0]],
         record2.contents[0]:[info2.contents[0]],
         record3.contents[0]:[info3.contents[0]],
         record4.contents[0]:[info4.contents[0]],
         }


#print(record1.contents[0]) = show the data

# Exports to Excel (.csv)
import pandas as pd
df = pd.DataFrame(krish)
       #print(df)
df.to_csv('fairfax.csv')

