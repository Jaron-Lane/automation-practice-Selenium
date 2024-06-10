import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser
driver = webdriver.Chrome()
time.sleep(2)

# Navigate to web page
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password Password123 into Password field
password_locator = driver.find_element(By.ID, "password")
password_locator.send_keys("Password123")

# Push Submit button
submit_button_locator = driver.find_element(By.CLASS_NAME, "btn")
submit_button_locator.click()
time.sleep(2)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
current_url = driver.current_url
assert current_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME, "h1")
text_actual = text_locator.text
assert text_actual == "Logged In Successfully"

# Verify button Log out is displayed on the new page
logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_button_locator.is_displayed()
