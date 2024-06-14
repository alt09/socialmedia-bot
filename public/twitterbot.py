from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def load_twitter_info():
    """
    Function to load Twitter information from the 'twitter.txt' file and set them as environment variables.
    """
    with open("twitter.txt", "r") as file:
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
    driver_path = "c:\\Program Files\\Google\\Chrome\\Application"  # Replace with the path to your WebDriver executable
    driver = webdriver.Chrome(driver_path)
    
    try:
        # Open the news website
        news_url = "https://miroradio.com/"  # Replace with the news website URL
        driver.get(news_url)
        
        # Wait for the news element to be visible
        wait = WebDriverWait(driver, 10)
        news_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "css-selector-of-news-element")))  # Replace with the actual CSS selector of the news element
        
        # Extract the text from the news element
        latest_news = news_element.text
        
    finally:
        # Close the WebDriver
        driver.quit()
    
    # Return the latest news
    return latest_news

def main():
    """
    Main function to load Twitter credentials, fetch latest news, and post it on Twitter.
    """
    # Load Twitter information from 'twitter.txt' into environment variables
    load_twitter_info()

    # Get information from environment variables
    usr = os.getenv("USER")  # Retrieve Twitter username
    pwd = os.getenv("PASSWORD")  # Retrieve Twitter password
    message = get_latest_news()  # Fetch the latest news to post
    image_path = os.getenv("IMAGE_PATH")  # Retrieve path to the image to be posted
    
    # Delete cache by setting preferences for the Firefox profile
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

    # Initialize Firefox WebDriver with custom profile (ensure you have the correct driver executable path)
    driver = webdriver.Firefox(executable_path=r'D:\Desktop\selenium\geckodriver')
    driver.implicitly_wait(15)  # Set an implicit wait of 15 seconds

    # Login to Twitter
    driver.get("https://twitter.com")
    sleep(3)  # Wait for the page to load
    elem = driver.find_element_by_name("session[username_or_email]")# TODO: research the current way to find this elements 
    elem.send_keys(usr)  # Enter the Twitter username
    elem = driver.find_element_by_name("session[password]")# TODO: research the current way to find this elements 
    elem.send_keys(pwd)  # Enter the Twitter password
    c = driver.find_element_by_class_name("EdgeButton")# TODO: research the current way to find this elements 
    c.click()  # Click the login button
    sleep(3)  # Wait for the login process to complete

    # Enter the text to post on Twitter
    mess = driver.find_element_by_id("tweet-box-home-timeline") # TODO: research the current way to find this elements 
    mess.send_keys(message)  # Enter the fetched latest news
    sleep(5)  # Wait for the message to be entered

    # If an image path is provided, upload the image
    if image_path:
        ima = driver.find_element_by_name("media_empty")# TODO: research the current way to find this elements 
        sleep(3)  # Wait before uploading the image
        ima.send_keys(image_path)  # Provide the image file path

    # Get the 'Post' button and click it
    Post_button = driver.find_element_by_class_name("tweet-action")# TODO: research the current way to find this elements 
    sleep(3)  # Wait before clicking the post button
    Post_button.click()  # Click the post button to publish the tweet
    sleep(3)  # Wait for the post to be made

    # Close the browser window
    driver.close()

if __name__ == '__main__':
    main()
