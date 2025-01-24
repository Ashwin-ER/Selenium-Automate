from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Function to test LinkedIn login
def test_linkedin_login(username, password):
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

    try:
        # Open LinkedIn login page
        driver.get("https://www.linkedin.com/login")

        # Wait for the page to load
        time.sleep(2)

        # Find the username and password fields
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")

        # Clear the fields and enter the credentials
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)

        # Click the Sign In button
        password_field.send_keys(Keys.RETURN)

        # Wait for the response
        time.sleep(5)

        # Check for login success or failure
        if "feed" in driver.current_url:
            print(f"Login successful for {username}")
        else:
            print(f"Login failed for {username}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

# Test cases
valid_username = "MAIL"#ENTER YOUR MAIL
valid_password = "PASS"#ENTER PASSWORD

# Test valid login
test_linkedin_login(valid_username, valid_password)

# Test invalid login
test_linkedin_login(invalid_username, invalid_password)
