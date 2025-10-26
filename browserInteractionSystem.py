from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#functions
def create_account():
    print("filler")

def login():
    print("filler")
    
def controller():
    print("filler")

#start browser
driver = webdriver.Chrome()
print("Chromium has opened!")

#navigate to url
driver.get("https://accounts.crypto.com/en-US/signup?utm_source=google")
print(f"You have successfully entered {driver.title}")

#configure site settings
time.sleep(4.5)
customize_settings_button = driver.find_element(by=By.ID, value="onetrust-pc-btn-handler")
customize_settings_button.click()
print("button pressed!")
reject_non-essential_cookies = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/div[3]/div[1]/button[1]")
reject_non-essential_cookies.click()
print("button pressed!")
