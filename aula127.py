from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


#url dos exoplanetas
START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

#webDrive

browser= webdriver.chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planet_data = []

#definir coleta e exoplanetas

def scrape():
    for i in range (0,10):
        print(f'coletando dados...{i+1}')
    #objeto BeautifulSoup
        soup = BeautifulSoup(browser.page_source,"html.parser")
    
    for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
        li_tags = ul_tag.find_all("li")
        
        temp_list=[]
        for index,li_tag in enumerate(li_tags):
            if index ==0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
    browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    scrape()
    #cabeçario
    headers=["name","light_years_from earth","planet_mass","stelar_magnitude","discovery_date"]
    data_frame=pd.DataFrame(planet_data,columns=headers)
    data_frame.to_csv("spacialData.csv",index=True,index_label="id")
      
        