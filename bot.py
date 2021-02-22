from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from time import sleep

#Setup of the chrome driver and path
PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)


#Navigate to the first site
driver.get("https://pennstatecampusrec.org/")
driver.implicitly_wait(5)


#Setup of future wait times
wait = WebDriverWait(driver, 2) 
wait1 = WebDriverWait(driver, 10)

try:
    #Begin Login Process native to site
    signup = driver.find_element_by_link_text("Log In")
    signup.click()
    element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "loginOption"))
    )
    element.click()

    #Microsoft Login Page
    email = wait.until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )
    email.send_keys("") #Enter your PSU e-mail here
    email.send_keys(Keys.RETURN)

    #PSU Login Page
    psuUser = wait.until(
        EC.presence_of_element_located((By.ID, "login"))
    )
    psuUser.send_keys("") #Enter your e-mail here again

    psuPass = driver.find_element_by_id("password")
    psuPass.send_keys("") #Enter your password here
    psuPass.send_keys(Keys.ENTER)

    finalSignUp = wait1.until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    finalSignUp.click()

    #Navigation to Timeslot Register page
    driver.implicitly_wait(20)
    #Test Case: driver.get("https://pennstatecampusrec.org/Program/GetProgramDetails?courseId=115d1e23-c0bf-4e58-9185-e38e98a44e6b&semesterId=531292ec-80c2-458c-83f3-21eac12b2222")
    driver.get("https://pennstatecampusrec.org/Program/GetProgramDetails?courseId=37c599b5-d91c-4111-ab0e-3a978a3d4d1c&semesterId=531292ec-80c2-458c-83f3-21eac12b2222")
except:
    driver.quit()

#Implement Refresh Loop until timeslot becomes available, which prompts a click
link = None
while not link:
    try:
        link = driver.find_element_by_class_name("btn-primary")
    except NoSuchElementException:
        driver.refresh()
link.click()

#Checkout Page, note: page javascript creates a stale element
try:
    checkout = wait.until(
        EC.presence_of_element_located((By.ID, "checkoutButton"))
    )
    checkout.click()
except StaleElementReferenceException:
    checkout = wait.until(
        EC.presence_of_element_located((By.ID, "checkoutButton"))
    )
    checkout.click()

#Modal View, final checkout button clicked
finalCheckout = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='modal-footer']/button[@onclick='Submit()']"))
)
finalCheckout.click()
    