from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://pennstatecampusrec.org/")
driver.implicitly_wait(5)
signup = driver.find_element_by_link_text("Log In")
signup.click()
wait = WebDriverWait(driver, 2) 
wait1 = WebDriverWait(driver, 10)

try:
    element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "loginOption"))
    )
    element.click()

    email = wait.until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )
    email.send_keys("slz5121@psu.edu")
    email.send_keys(Keys.RETURN)

    psuUser = wait1.until(
        EC.presence_of_element_located((By.ID, "login"))
    )
    psuUser.send_keys("slz5121")

    psuPass = driver.find_element_by_id("password")
    psuPass.send_keys("Headsh0t!!")
    psuPass.send_keys(Keys.ENTER)

    finalSignUp = wait.until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    finalSignUp.click()
    driver.implicitly_wait(20)
    #driver.get("https://pennstatecampusrec.org/Program/GetProgramDetails?courseId=115d1e23-c0bf-4e58-9185-e38e98a44e6b&semesterId=531292ec-80c2-458c-83f3-21eac12b2222")
    driver.get("https://pennstatecampusrec.org/Program/GetProgramDetails?courseId=37c599b5-d91c-4111-ab0e-3a978a3d4d1c&semesterId=531292ec-80c2-458c-83f3-21eac12b2222")
except:
    driver.quit()
link = None
while not link:
    try:
        link = driver.find_element_by_class_name("btn-primary")
    except NoSuchElementException:
        driver.refresh()
link.click()
try:
    checkout = wait.until(
        EC.presence_of_element_located((By.ID, "checkoutButton"))
    #id = checkoutButton
    )
    checkout.click()
except StaleElementReferenceException:
    checkout = wait.until(
        EC.presence_of_element_located((By.ID, "checkoutButton"))
    #id = checkoutButton
    )
    checkout.click()

finalCheckout = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='modal-footer']/button[@onclick='Submit()']"))
)
finalCheckout.click()
    