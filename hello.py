from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up ChromeDriver path
service = Service("C:/Users/huria/My git projects/my-first-python-code/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")
time.sleep(2)  # Wait for page to load

# Find the search box and type a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium tutorial")
search_box.submit()  # Press Enter

time.sleep(5)  # Let results load

# End of script
input("Press Enter to close browser...")
driver.quit()
