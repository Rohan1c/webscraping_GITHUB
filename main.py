from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
from selenium.webdriver.chrome.service import Service

driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = r"C:\Users\rohan\webscraping\chromedriver.exe" # Change this to your own chromedriver path!
def create_webdriver():
    service = Service(executable_path=chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)

# Open the website
browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")