from selenium import webdriver  # Controls browser
from selenium.webdriver.common.by import By  # Finds elements
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Manages ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open Laravel login page
driver.get("http://127.0.0.1:8000/login")

# Find email & password fields
email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")

# Fill login form
email.send_keys("testuser@example.com")
password.send_keys("randompassword123")

# Submit form
driver.find_element(By.TAG_NAME, "form").submit()

# Close browser
driver.quit()
