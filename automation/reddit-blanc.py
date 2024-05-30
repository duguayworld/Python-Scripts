from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Replace these with your Reddit credentials
reddit_username = "duguayworld"
reddit_password = "Notnewtothegame89!"

# Replace this with the list of paths to your image files
image_paths = ["/home/bnzo/PycharmProjects/pythonProject/Automation/Media/screenshot5.png"]

# Set up ChromeOptions to use Chromium executable
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = '/usr/bin/chromium'

# Set up the WebDriver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Reddit and login
print("Navigating to Reddit login page...")
driver.get("https://www.reddit.com/login/")
time.sleep(2)  # Add a short delay for the page to load

# Find the username and password fields, and submit the login form
print("Entering Reddit credentials...")
username_field = driver.find_element("name", "username")
password_field = driver.find_element("name", "password")
username_field.send_keys(reddit_username)
password_field.send_keys(reddit_password)
password_field.send_keys(Keys.RETURN)

# Wait for the login to complete
time.sleep(3)

# Navigate to the submission page
print("Navigating to the submission page...")
driver.get("https://www.reddit.com/user/duguayworld/submit")

# Simulate pressing the TAB key to navigate to the title input
for _ in range(15):
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)

# Simulate pressing the ENTER key to activate the title input
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(1)

# Simulate pressing the TAB key to navigate to the file input
for _ in range(3):
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)

# Simulate pressing the ENTER key to activate the file input
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(1)

# Type your post title
post_title = "Here is a simple combination of html, css and javascript store webpage, a simple one page idea with product cards and a hero. https://duguayworld.github.io/1/index.html"
print(f"Typing post title: {post_title}")
ActionChains(driver).send_keys(post_title).perform()
time.sleep(1)

# Send the file paths to the file input
file_input = driver.find_element("css selector", 'input[type="file"]')
print(f"Uploading images from: {image_paths}")
file_input.send_keys("\n".join(image_paths))

# Wait for the images to upload
time.sleep(5)

# Find the post button and click it
print("Submitting the post...")
post_button_xpath = '//*[@id="AppRouter-main-content"]/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div/div[1]/button'
post_button = driver.find_element(By.XPATH, post_button_xpath)
post_button.click()

# Wait for the post to be submitted (adjust the time as needed)
time.sleep(5)

# Close the browser
print("Post submitted successfully. Closing the browser...")
driver.quit()
