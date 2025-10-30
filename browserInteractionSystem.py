from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#variables
command = ""

#functions
def create_account():
    print("test1")
    
def login():
    print("test2")

def command_guide():
    print("test3")

#call browser!
driver = webdriver.Chrome()
print(f"{driver.name} activated!")

#move to!
driver.get("https://accounts.crypto.com/en-US/signup?utm_campaign=Google+Search_MA_Web_CA_en_NA_CPA_Brand_20250401&utm_medium=cpc&utm_source=google")
print(f"crypto.com has been opened!")
time.sleep(4.0)

#cookie configuration!
customize_settings = driver.find_element(by=By.ID , value="onetrust-pc-btn-handler")
print("Element found!")
customize_settings.click()
print("Have clicked settings!")
time.sleep(3.0)
reject_non_essential_cookies = driver.find_element(by=By.XPATH , value="/html/body/div[3]/div[3]/div/div[3]/div[1]/button[1]")
print("Element found!")
reject_non_essential_cookies.click()
print("Have clicked settings!")
time.sleep(3.0)

#click email fill in!
click_email_box = driver.find_element(by=By.XPATH , value="/html/body/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div")
print("Email box selected!")
time.sleep(3.0)
click_email_box.click()
print("Email box clicked!")
time.sleep(3.0)
input_email_box = driver.find_element(by=By.XPATH , value="/html/body/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/input[1]")
input_email_box.send_keys("Example@gmail.com")
print("Email has been entered!")
time.sleep(3.0)
submit_email = driver.find_element(by=By.XPATH , value="/html/body/div[2]/main/div[2]/div/div/div[1]/div/form/div[6]/button[1]")
submit_email.click()

#capacha automation
