import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = 'duguay_world@outlook.com'
password = 'Notnewtothegame89!'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.facebook.com")

# Use the appropriate locator strategy here
username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")
login_button = driver.find_element(By.NAME, "login")

username_field.send_keys(email)
password_field.send_keys(password)

login_button.click()

# Wait for the login to complete
WebDriverWait(driver, 10).until(EC.url_contains("facebook.com"))

driver.get("https://www.facebook.com/friends/suggestions")

for _ in range(25):
    # Press TAB 15 times and then hit ENTER with time waits
    action_chains = ActionChains(driver)

    for _ in range(16):
        action_chains.send_keys(Keys.TAB)
        time.sleep(1)  # Add a small delay between key presses

    # Press the Enter key
    action_chains.send_keys(Keys.ENTER)
    action_chains.perform()

    # Refresh the page
    driver.get("https://www.facebook.com/friends/suggestions")

# Close the browser after the loop
driver.quit()

print('Script completed. Browser closed.')
