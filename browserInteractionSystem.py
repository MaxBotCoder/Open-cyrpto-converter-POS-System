from selenium import webdriver
from selenium.webdriver.common.by import By
from threads import Timer

#Some test code!

url = (f"https://{input('inputurl: ')}")
print(f"fetching {url}")

driver = webdriver.Chrome()

driver.get(url)
print(f"Success {driver.title} has been opened!")

