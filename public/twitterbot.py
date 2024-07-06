from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

def load_twitter_info():
    """
    Function to load Twitter information from the 'twitter.txt' file and set them as environment variables.
    """
    twitter_info_path = r"C:\Users\Andres  Lara-trevino\programacion\projectos\python\socialmedia-bot\private\twitter.txt"#path of the file where you store your password and user 
    with open(twitter_info_path, "r") as file:
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

    driver = webdriver.Chrome()
    
    try:
       # #Open the news website
       # news_url = "https://miroradio.com/"  # Replace with the news website URL
       # driver.get(news_url)
        
        # Wait for the news element to be visible
        #wait = WebDriverWait(driver, 10)
        news_element = "yolo"  #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "https://miroradio.com/wp-content/plugins/ansar-import/public/css/ansar-import-public.css?ver=1.0.16")))  # Replace with the actual CSS selector of the news element
        
        # Extract the text from the news element
        latest_news = news_element
        
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
    
    Options = webdriver.ChromeOptions().add_argument('--disable-cache')
    driver = webdriver.Chrome(options=Options)
    driver.implicitly_wait(15)

    try:
        driver.get("https://twitter.com/login")
        sleep(3)
        
        username_field = driver.find_element(By.NAME, "session[username_or_email]")
        username_field.send_keys(usr)
        
        password_field = driver.find_element(By.NAME, "session[password]")
        password_field.send_keys(pwd)
        
        login_button = driver.find_element(By.CSS_SELECTOR, "div[data-testid='LoginForm_Login_Button']")
        login_button.click()
        sleep(3)
        
        tweet_box = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tweet text']")
        tweet_box.send_keys(message)
        sleep(5)
        
        if image_path:
            media_input = driver.find_element(By.CSS_SELECTOR, "input[type='file'][aria-label='Add photos or video']")
            sleep(3)
            media_input.send_keys(image_path)
        
        post_button = driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']")
        sleep(3)
        post_button.click()
        sleep(3)
    
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
