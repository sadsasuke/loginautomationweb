from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_element(browser, by, value):
    # Wait for the element to be available
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((by, value))
    )

    # Click the element
    element.click()
svc = webdriver.ChromeService(executable_path=binary_path)
browser = webdriver.Chrome(service=svc)



url = "https://go.writeomatic.app/login"
browser.get(url)

# Waiting for the email field to be available
user_block = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'email')))
user_block.send_keys("your_username")

# Waiting for the password field to be available
pw_block = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'password')))
pw_block.send_keys("your_password")

# Waiting for the submit button to be available
submit_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'LoginFormButton')))
submit_button.click()


# The CSS selector to locate the specific link using the class name
css_selector = "a.btn[href='https://go.writeomatic.app/dashboard/user/openai/documents/all']"

# Assuming 'browser' is your WebDriver object, and you have navigated to the correct page
click_element(browser, By.CSS_SELECTOR, css_selector)
print("yes")
