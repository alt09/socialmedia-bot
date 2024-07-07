from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
import os

def load_facebook_info():
    """
    Function to load Facebook information from the 'facebook.txt' file and set them as environment variables.
    """
    facebook_info_path = r"C:\Users\Andres  Lara-trevino\programacion\projectos\python\socialmedia-bot\private\facebook.txt"#path of the file where you store your password and user 
    with open(facebook_info_path, "r") as file:
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
    # Configure Chrome options to disable notifications
   # chrome_options = webdriver.ChromeOptions()
    #prefs = {"profile.default_content_setting_values.notifications": 2}
    #chrome_options.add_experimental_option("prefs", prefs)

    # Initialize WebDriver with the configured options
    #driver = webdriver.Chrome(options=chrome_options)
    #try:
        ## Open the news website
        #news_url = "https://miroradio.com/"  # Replace with the news website URL
        #driver.get(news_url)
        
        ## Wait for the news element to be visible
        #wait = WebDriverWait(driver, 10)
    news_element = "im searching for a programming mentor for the frc team 6413"#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "css-selector-of-news-element")))  # Replace with the actual CSS selector of the news element
        
        # Extract the text from the news element
    latest_news = news_element
        
    #finally:
        # Close the WebDriver
     #   driver.quit()
    return latest_news

def main():
    """
    Main function to load Facebook credentials, fetch latest news, and post it on multiple Facebook groups.
    """
    # Load Facebook information from 'facebook.txt' into environment variables
    load_facebook_info()

    # Get information from environment variables
    usr = os.getenv("USER")  # Retrieve Facebook username
    pwd = os.getenv("PASSWORD")  # Retrieve Facebook password
    message = "im searching for a programming mentor for the frc team 6413"#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "css-selector-of-news-element")))  # Replace with the actual CSS selector of the news element
#get_latest_news()  # Fetch the latest news to post
    image_path = os.getenv("IMAGE_PATH")  # Retrieve path to the image to be posted
    group_links = os.getenv("GROUP_LINKS").split()  # Retrieve Facebook group links as a list

    # Configure Chrome options to disable notifications
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--disable-cache')

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(1)
    
    try:
         # Login to Facebook
        driver.get("https://www.facebook.com/login/")
        sleep(1)
        username_field = driver.find_element(By.CSS_SELECTOR, "#email")
        username_field.send_keys(usr)

        password_field = driver.find_element(By.CSS_SELECTOR, "#pass")
        password_field.send_keys(pwd)
        
        login_button = driver.find_element(By.CSS_SELECTOR, "#loginbutton")
        login_button.click()
        sleep(3)

    # Loop through each Facebook group link to post the message and image
        for group in group_links:
            # Navigate to the Facebook group
            driver.get(group)
            sleep(3)  # Wait for the page to load
            # Find the post box and enter the message
            post_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]')            
            post_button.click()
            sleep(3)  # Wait for the message to be entered

            message_box = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/p")
            message_box.send_keys(message)
            # If an image path is provided, upload the image
            if image_path != "":
                addMedia = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div")
                addMedia.send_keys(image_path)

            # Find the 'Post' button and click it
            Post_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div")
            Post_button.click()
            sleep(10)  # Wait for the post to be made
    finally:
    # Close the browser window
        sleep(3)
if __name__ == '__main__':
    main()
