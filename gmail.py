from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def register_gmail(email, password):
    driver = webdriver.Chrome()  # Make sure you've got Chrome WebDriver installed
    driver.get("https://accounts.google.com/signup")

    time.sleep(2)  # Giving the page time to breathe

    # Now, let's fill in the sacred registration form
    driver.find_element("firstName").send_keys("John")
    driver.find_element("lastName").send_keys("Doe")
    driver.find_element("username").send_keys(email)
    driver.find_element_by_name("Passwd").send_keys(password)
    driver.find_element_by_name("ConfirmPasswd").send_keys(password)

    # Let's offer up this sacred data to the Google gods
    driver.find_element("accountDetailsNext").click()

    time.sleep(5)  # Waiting for the divine verification page

    # Ah, the sacred "I Agree" button. Click it and bask in the glory.
    driver.find_element("termsofserviceNext").click()

    time.sleep(5)  # Waiting for the heavenly confirmation page

    # And with that, our work here is done. Time to close the portal.
    driver.quit()


# Example usage:
email = "example@gmail.com"
password = "examplepassword"
register_gmail(email, password)
