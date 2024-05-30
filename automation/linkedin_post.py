import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

username = ''
password = '!'
post_text = "Some test I am doing tonight!"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# Set the path to your Chromium executable
chromium_path = "/usr/bin/chromium"
chrome_options.binary_location = chromium_path

driver = webdriver.Chrome(options=chrome_options)

# Open LinkedIn login page
driver.get("https://www.linkedin.com/login")

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username_field.send_keys(email)
password_field.send_keys(password)

login_button.click()

# Wait for and close the message overlay (if present)
try:
    overlay_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "truncate")]'))
    )
    overlay_element.click()
    print("Message overlay closed successfully.")
except TimeoutException:
    print("Message overlay not found or could not be closed.")

# Explicitly wait for the Home page to load
driver.get("https://www.linkedin.com/feed")
WebDriverWait(driver, 20).until(EC.url_contains("linkedin.com/feed"))

# Click on "Start a post"
try:
    status_update_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ember25"]'))
    )
    status_update_element.click()
    print("Clicked on 'Start a post' successfully.")
except TimeoutException:
    print("Start a post button not found.")

# Enter post text
try:
    popup_textbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[@role='textbox']"))
    )
    # Start typing
    popup_textbox.send_keys("Voici mon portfolio ainsi que CV en ligne.")
    # Line Break
    popup_textbox.send_keys(Keys.ENTER)
    popup_textbox.send_keys("Here is my portfolio and my online resume.")

    # Line Break
    popup_textbox.send_keys(Keys.ENTER)
    popup_textbox.send_keys("https://duguayworld.github.io/  #duguayworld #dbwebmedia")
    time.sleep(1)
    actions = ActionChains(driver)
    # Add a short delay between key presses
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.ENTER)

    actions.perform()

    print('Post published successfully!')
except TimeoutException:
    print("Post text box not found.")

time.sleep(5)

# Explicitly wait for the Home page to load
driver.get("https://www.linkedin.com/feed")
WebDriverWait(driver, 20).until(EC.url_contains("linkedin.com/feed"))

# Click on "Start a post"
try:
    status_update_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ember25"]'))
    )
    status_update_element.click()
    print("Clicked on 'Start a post' successfully.")
except TimeoutException:
    print("Start a post button not found.")

# Enter post text
try:
    popup_textbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[@role='textbox']"))
    )
    # Start typing
    popup_textbox.send_keys("Explorez mon compte Instagram pour découvrir des moments captivants, des images inspirantes et bien plus encore. Rejoignez la communauté et partagez vos propres instants mémorables avec nous!")
    # Line Break
    popup_textbox.send_keys(Keys.ENTER)
    popup_textbox.send_keys("Follow me on Instagram.")

    # Line Break
    popup_textbox.send_keys(Keys.ENTER)
    popup_textbox.send_keys("https://www.instagram.com/p/C2JLJ7UseLL/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==  #duguayworld #dbwebmedia")
    time.sleep(1)
    actions = ActionChains(driver)
    # Add a short delay between key presses
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.ENTER)

    actions.perform()

    print('Post published successfully!')
except TimeoutException:
    print("Post text box not found.")

time.sleep(5)

# Explicitly wait for the Home page to load
driver.get("https://www.linkedin.com/feed")
WebDriverWait(driver, 20).until(EC.url_contains("linkedin.com/feed"))

# Click on "Start a post"
try:
    status_update_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ember25"]'))
    )
    status_update_element.click()
    print("Clicked on 'Start a post' successfully.")
except TimeoutException:
    print("Start a post button not found.")

# Enter post text
try:
    popup_textbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[@role='textbox']"))
    )
    # Start typing
    popup_textbox.send_keys("Découvrez DB Web Media, ma page Facebook dédiée aux services professionnels dans le domaine du web et des médias. Suivez-nous pour rester informé(e) sur nos derniers projets, actualités et astuces dans le monde numérique. Rejoignez la communauté et explorez les opportunités ensemble ! #DBWebMedia ")
    # Line Break
    popup_textbox.send_keys(Keys.ENTER)
    popup_textbox.send_keys("Follow DB Web Media on Facebook!")

    # Line Break
    popup_textbox.send_keys(Keys.ENTER)
    popup_textbox.send_keys("https://www.facebook.com/profile.php?id=61555239764539  #duguayworld #dbwebmedia")
    time.sleep(3)
    actions = ActionChains(driver)
    # Add a short delay between key presses
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.ENTER)

    actions.perform()

    print('Post published successfully!')
except TimeoutException:
    print("Post text box not found.")

time.sleep(5)

# Explicitly wait for the Home page to load
driver.get("https://www.linkedin.com/feed")
WebDriverWait(driver, 20).until(EC.url_contains("linkedin.com/feed"))

# Click on "Start a post"
try:
    status_update_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ember25"]'))
    )
    status_update_element.click()
    print("Clicked on 'Start a post' successfully.")
except TimeoutException:
    print("Start a post button not found.")


    # Simulate drag-and-drop by providing the file path to the hidden file input
    file_path = '/home/bnzo/PycharmProjects/pythonProject/Automation/Media/pub-5.png'
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    file_input.send_keys(file_path)
    time.sleep(1)
    actions = ActionChains(driver)
    # Add a short delay between key presses
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    time.sleep(1)
    actions.send_keys(Keys.ENTER)

    actions.perform()

    print('Post published successfully!')
except TimeoutException:
    print("Post text box not found.")
finally:
    driver.quit()
