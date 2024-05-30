import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = ''
password = ''

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

driver.get("https://www.facebook.com/profile.php?id=61554272417391")

# Define the target element
status_update_xpath = "//span[contains(text(), \"What's on your mind?\")]"

# Scroll down until the target element is in view
while not driver.find_elements(By.XPATH, status_update_xpath):
    driver.execute_script("window.scrollBy(0, 500);")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, status_update_xpath)))

# Click on the target element
status_update_element = driver.find_element(By.XPATH, status_update_xpath)
status_update_element.click()

# Wait for the pop-up window to appear
popup_textbox_xpath = "//div[@role='dialog']//div[@role='textbox']"
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, popup_textbox_xpath)))

# Find the text box within the pop-up and enter text
popup_textbox = driver.find_element(By.XPATH, popup_textbox_xpath)
popup_textbox.send_keys(
    "Chers amis, j'aimerais partager avec vous ma passion et mon engagement à travers ma page professionnelle sur Facebook. Si vous trouvez de la valeur dans ce que je fais, je vous invite cordialement à soutenir mon projet en partageant cette page. Votre support contribuera à élargir mon réseau et à renforcer mon impact. Merci du fond du cœur pour votre précieuse collaboration ! #PartageProfessionnel #RéseauEngagé https://duguayworld.github.io/"
)

# Use ActionChains to press Shift + Tab multiple times and press Enter
actions = ActionChains(driver)
# Add a short delay between key presses
time.sleep(1)
actions.key_down(Keys.SHIFT)
for _ in range(3):
    actions.send_keys(Keys.TAB)
time.sleep(1)
actions.key_up(Keys.SHIFT)
time.sleep(1)
actions.send_keys(Keys.ENTER)

actions.perform()

# Use ActionChains to press Shift + Tab multiple times and press Enter
actions = ActionChains(driver)
# Add a short delay between key presses
time.sleep(1)
actions.key_down(Keys.SHIFT)
for _ in range(2):
    actions.send_keys(Keys.TAB)
time.sleep(1)
actions.key_up(Keys.SHIFT)
time.sleep(1)
actions.send_keys(Keys.ENTER)

actions.perform()

# Use ActionChains to press Shift + Tab multiple times and press Enter
actions = ActionChains(driver)
# Add a short delay between key presses
time.sleep(1)
actions.key_down(Keys.SHIFT)
for _ in range(4):
    actions.send_keys(Keys.TAB)
time.sleep(1)
actions.key_up(Keys.SHIFT)
time.sleep(1)
actions.send_keys(Keys.ENTER)

actions.perform()

# Print a message indicating that the post is published
print('Post published successfully!')


