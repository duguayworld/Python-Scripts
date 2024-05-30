import time
from datetime import datetime, timedelta
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

username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")
login_button = driver.find_element(By.NAME, "login")

username_field.send_keys(email)
password_field.send_keys(password)

login_button.click()

# POST SECTION ////////////////////////////////////////////////////////////////
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Découvrez DB Web Media, ma page Facebook dédiée aux services professionnels dans le domaine du web et des médias. Suivez-nous pour rester informé(e) sur nos derniers projets, actualités et astuces dans le monde numérique. Rejoignez la communauté et explorez les opportunités ensemble ! #DBWebMedia https://www.facebook.com/profile.php?id=61555239764539"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Suivez-nous pour explorer nos projets inspirants, rester informé(e) des dernières tendances numériques et partager cette expérience visuelle unique. Rejoignez-nous et faites partie de notre communauté ! #DBWebMedia #InspirationDigitale https://www.instagram.com/p/C2AaqftrYRP/?utm_source=ig_web_copy_link"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Merci d'avance pour vos partage!\nhttps://rebrand.ly/shv2w0s"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Chers amis et collègues, je vous invite à explorer et à soutenir mon parcours professionnel sur LinkedIn. Connectons-nous pour échanger sur nos expériences, partager des idées et construire ensemble un réseau dynamique. Votre soutien est précieux! #RéseauProfessionnel #LinkedIn https://www.linkedin.com/in/duguayworld/"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Merci d'avance pour vos partage!\nhttps://rebrand.ly/xcyktja\n#DBWebMedia\n#OdysseeConstruction"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Suivez le développement de votre page web en live. Vivez l'expérience avec le site de l'un de nos clients.\nhttps://duguayworld.github.io/Jeff/index.html"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Essayez nos pages web en direct. Cette page web est une démo.\nhttps://duguayworld.github.io/Demos/PromoWeb/index.html\nIl n'a jamais été aussi facile de lancer un produit en ligne.\n#DBWebMedia"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Pour des publicités de qualité, pensez à DBWebMedia.\nhttps://rebrand.ly/t718z8w\n#DBWebMedia\n#ElevagesJR"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Des publicités percutantes.\nhttps://rb.gy/8325sw\n#DBWebMedia"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Pour des publicités de qualité, pensez à DBWebMedia.\nhttps://rb.gy/g8t6zt\n#DBWebMedia"
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Voici une publicité réalisée pour un client satisfait, Électricité DJ Inc.\nhttps://rebrand.ly/qny4vx2\n#DBWebMedia\n#ÉlectricitéDJInc."
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Voici une publicité réalisée pour un client satisfait, Électricité DJ Inc.\nhttps://rebrand.ly/ghq9flu\n#DBWebMedia\n#ÉlectricitéDJInc."
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

time.sleep(5)

# POST SECTION ////////////////////////////////////////////////////////////////

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
    "Suivez le développement de votre page web en live. Vivez l'expérience avec le site de l'un de nos clients.\nhttps://duguayworld.github.io/JS/index.html\n#ÉlectricitéDJ\n#DBWebMedia "
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

time.sleep(5)

# CLICK LIKES SECTION /////////////////////////////////////////////////////

# Wait for thepage to load
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

print('Script completed. Browser closed.')

time.sleep(5)

# ADD FRIENDS SECTION ////////////////////////////////////////////////////////////////

# Wait for the page to load
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
