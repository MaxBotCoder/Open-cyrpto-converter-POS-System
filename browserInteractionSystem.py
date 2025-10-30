from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#variables
url_crypto_dot_com = "https://accounts.crypto.com/en-US/signup?utm_campaign=Google+Search_MA_Web_CA_en_NA_CPA_Brand_20250401&utm_medium=cpc&utm_source=google" 
url_buser_capacha_solver = "https://chromewebstore.google.com/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en-GB&utm_source=ext_sidebar"
driver = webdriver.Chrome()

#functions
def command_gateway():
    print("filler")
    
def load_extensions():
    driver.get(url_buser_capacha_solver)
    print("Extension page entered!")
    time.sleep(5.0)
    add_to_chrome = driver.find_element(by=By.XPATH , value="/html/body/c-wiz/div/div/main/div/section[1]/section/div/div[1]/div[2]/div/button")
    add_to_chrome.click()
 
def create_account_general(email):
    driver.get(url_crypto_dot_com)
    print("Erypto.com! entered")
    time.sleep(5.0)
    reject_non_essential_cookies = driver.find_element(by=By.ID , value="onetrust-reject-all-handler")
    reject_non_essential_cookies.click()
    print("Rejected non essential cookies!")
    time.sleep(5.0)
    input_email = driver.find_element(by=By.XPATH , value="/html/body/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/input")
    input_email.send_keys(email)
    print(f"{email} has been entered!")
    time.sleep(5.0)
    create_account_button = driver.find_element(by=By.XPATH , value="/html/body/div[2]/main/div[2]/div/div/div[1]/div/form/div[6]/button[1]/span")
    create_account_button.click()
    print("button clicked!")
        
def login_general():
    print("filler")
    
#call functions

load_extensions()
create_account_general("maxrodsto@outlook.com")
