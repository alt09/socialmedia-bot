from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os

def load_twitter_info():
    """
    Function to load twitter information from the 'twitter.txt' file and set them as environment variables.
    """
    with open("twitter.txt", "r") as file:
        # Read each line from the file
        for line in file:
            # Split each line into key-value pair based on '=' separator
            key, value = line.strip().split("=")
            # Set environment variable with key as variable name and value as its value
            os.environ[key] = value

def main():
    
    # Load twitter information from 'twitter.txt' into environment variables
    load_twitter_info()

    # Get information from environment variables
    usr = os.getenv("USER")  # Retrieve username
    pwd = os.getenv("PASSWORD")  # Retrieve password
    message = ""  # Placeholder: Enter the message you want to post here
    image_path = os.getenv("IMAGE_PATH")  # Retrieve image path
	
	# Delete cache by setting preferences for the Firefox profile
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

	# Path to geckodriver executable
    driver = webdriver.Firefox(executable_path=r'D:\Desktop\selenium\geckodriver')
    driver.implicitly_wait(15) # Set an implicit wait of 15 seconds

	# Login to twitter
    driver.get("https://twitter.com")
    sleep(3)
    elem = driver.find_element_by_name("session[username_or_email]")
    elem.send_keys(usr)# Enter the user email
    elem = driver.find_element_by_name("session[password]")
    elem.send_keys(pwd)# Enter the user password
    c = driver.find_element_by_class_name("EdgeButton")
    c.click()# Click the login button
    sleep(3)
	# Enter the text we want to post to twitter and the image 
    mess = driver.find_element_by_id("tweet-box-home-timeline")
    mess.send_keys(message)
    sleep(5)
    ima = driver.find_element_by_name("media_empty")
    sleep(3)
    ima.send_keys(image_path)
    # Get the 'Post' button and click on it
    Post_button = driver.find_element_by_class_name("tweet-action")
    sleep(3)
    Post_button.click()
    sleep(3)
    driver.close()

if __name__ == '__main__':
  main()