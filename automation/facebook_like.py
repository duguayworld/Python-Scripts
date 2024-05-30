import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = ''
password = '!'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.facebook.com")

username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")
login_button = driver.find_element(By.NAME, "login")

username_field.send_keys(email)
password_field.send_keys(password)

login_button.click()

# Wait for the login to complete
WebDriverWait(driver, 10).until(EC.url_contains("facebook.com"))

driver.get("https://www.facebook.com/")

# Set the duration for 5 minutes
end_time = datetime.now() + timedelta(minutes=5)

while datetime.now() < end_time:
    # Define the target elements for all Like buttons
    like_buttons = driver.find_elements(By.XPATH, "//span[contains(text(), 'Like')]")

    # Click on each Like button and scroll down
    for like_button in like_buttons:
        try:
            like_button.click()
        except:
            # Handle any exceptions if the button is not clickable
            pass

        # You might want to add a delay between actions to avoid rate limiting
        time.sleep(2)

        # Scroll down using ActionChains and arrow down key
        action_chains = ActionChains(driver)
        action_chains.send_keys(Keys.ARROW_DOWN).perform()

# Close the browser after 5 minutes
driver.quit()

print('Script completed. Browser closed.')
