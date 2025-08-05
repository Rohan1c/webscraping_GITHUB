from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

driver_option = webdriver.ChromeOptions()  #setting up for chrome
driver_option.add_argument("--incognito")

chromedriver_path = r"C:\Users\rohan\webscraping\chromedriver.exe"     
service = Service(executable_path=chromedriver_path)

browser = webdriver.Chrome(service=service, options=driver_option)

browser.get("https://github.com/collections/machine-learning")       #opening the page to scrape
time.sleep(3)  # waiting for contents to load

projects = browser.find_elements(By.CSS_SELECTOR, "h1.h3.lh-condensed")

data = []
for project in projects:
    a_tag = project.find_element(By.TAG_NAME, "a")
    name = a_tag.text
    url = a_tag.get_attribute("href")
    data.append({"Project Name": name, "URL": url})

df = pd.DataFrame(data) #converting into dataframe 

df.to_csv("github_ml_projects.csv", index=False)
print(" Data saved to github_ml_projects.csv")

browser.quit()
