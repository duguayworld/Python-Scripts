import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

username = 'duguay_world@outlook.com'
password = 'Notnewtothegame89!'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav")

# Wait for the login page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
except Exception as e:
    print("Timed out waiting for the login page to load.")
    driver.quit()
    exit()

# Log in
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)

actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
time.sleep(1)
actions.send_keys(Keys.TAB)
time.sleep(1)
actions.send_keys(Keys.ENTER)

actions.perform()

# Wait for the login to complete
try:
    WebDriverWait(driver, 10).until(EC.url_contains("instagram.com"))
except Exception as e:
    print("Timed out waiting for login to complete.")
    driver.quit()
    exit()

time.sleep(5)

# Navigate to the "Create" button
for _ in range(8):
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    time.sleep(1.5)
    actions.perform()

# Press Enter on the "Create" button
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

# Navigate to the "Create" button
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
time.sleep(1.5)
actions.perform()

# Press Enter on the "Create" button
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
# Wait for a while (you can adjust this based on your needs)
time.sleep(3)

# Simulate drag-and-drop by providing the file path to the hidden file input
file_path = '/home/bnzo/PycharmProjects/pythonProject/Automation/Media/1.png'
file_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
file_input.send_keys(file_path)

# Wait for a while to ensure the file upload is complete
time.sleep(2)

# Navigate to the share action
for _ in range(3):
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    time.sleep(0.5)
    actions.send_keys(Keys.TAB)
    time.sleep(0.5)
    actions.send_keys(Keys.ENTER)
    time.sleep(2)  # Adjust this sleep time based on your needs

    actions.perform()

# Close the browser window
driver.quit()
