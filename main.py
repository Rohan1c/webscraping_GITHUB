from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
       
chromedriver_path = r"C:\Users\rohan\webscraping\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--headless")  
options.add_argument("--incognito")

service = Service(executable_path=chromedriver_path)

urls = [
    "https://github.com/collections/machine-learning",
    "https://github.com/collections/deep-learning",
    "https://github.com/collections/artificial-intelligence"
]

def scrape(url):
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(url)
    projects = browser.find_elements(By.CSS_SELECTOR, "h1.h3.lh-condensed")

    data = []
    for project in projects:
        a_tag = project.find_element(By.TAG_NAME, "a")
        name = a_tag.text.strip()
        href = a_tag.get_attribute("href")
        data.append({"Project Name": name, "URL": href, "Source": url})

    browser.quit()
    return data

all_data = []
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(scrape, urls)
    for res in results:
        all_data.extend(res)

df = pd.DataFrame(all_data)
df.to_csv("github_parallel_selenium.csv", index=False)
print("Data saved to github_parallel_selenium.csv")
