from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def load_facebook_info():
    """
    Function to load Facebook information from the 'facebook.txt' file and set them as environment variables.
    """
    with open("facebook.txt", "r") as file:
        # Read each line from the file
        for line in file:
            # Split each line into key-value pair based on '=' separator
            key, value = line.strip().split("=")
            # Set environment variable with key as variable name and value as its value
            os.environ[key] = value

def get_latest_news():
    """
    Function to fetch the latest news from a news website and return it as a string.
    """
    # Initialize WebDriver (ensure you have the correct driver executable path)
    driver_path = "c:\Program Files\Google\Chrome\Application"  # Replace with the path to your WebDriver executable
    driver = webdriver.Chrome(driver_path)
    
    try:
        # Open the news website
        news_url = "https://miroradio.com/"  # Replace with the news website URL (in case you don't use this one 
        driver.get(news_url)
        
        # Wait for the news element to be visible
        wait = WebDriverWait(driver, 10)
        news_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "css-selector-of-news-element")))  # Replace with the actual CSS selector of the news element
        
        # Extract the text from the news element
        latest_news = news_element.text
        
    finally:
        # Close the WebDriver
        driver.quit()
    print(latest_news)
    return latest_news
print(get_latest_news)


def main():
    # Load Facebook information from 'facebook.txt' into environment variables
    load_facebook_info()

    # Get information from environment variables
    usr = os.getenv("USER")  # Retrieve username
    pwd = os.getenv("PASSWORD")  # Retrieve password
    message = get_latest_news()# Placeholder: Enter the message you want to post here
    image_path = os.getenv("IMAGE_PATH")  # Retrieve image path
    group_links = os.getenv("GROUP_LINKS").split()  # Retrieve group links as a list

    # Delete cache by setting preferences for the Firefox profile
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

    # Path to geckodriver executable
    driver = webdriver.Firefox(executable_path=r'D:\Desktop\selenium\geckodriver', firefox_profile=profile)
    driver.implicitly_wait(15)  # Set an implicit wait of 15 seconds

    # Login to Facebook
    driver.get("http://www.facebook.com")
    sleep(3)
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)  # Enter the user email
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)  # Enter the user password
    c = driver.find_element_by_id('loginbutton')
    c.click()  # Click the login button
    sleep(3)

    # Loop through each group link to post the message and image
    for group in group_links:
        # Go to the Facebook group
        driver.get(group)
        sleep(5)  # Wait for the page to load

        # Find the post box and enter the message
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
        post_box.send_keys(message)
        sleep(5)  # Wait for the message to be entered

        # If an image path is provided, upload the image
        if image_path != "":
            addMedia = driver.find_element_by_xpath("//*[@data-testid='media-attachment-selector']")
            addMedia.click()
            # Provide the picture file path
            driver.find_element_by_xpath("//*[@name='composer_photo']").send_keys(image_path)

        # Find the 'Post' button and click it
        Post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
        sleep(5)  # Wait before clicking the post button
        Post_button.click()
        sleep(5)  # Wait for the post to be made

    # Close the browser window
    driver.close()

if __name__ == '__main__':
    main()
