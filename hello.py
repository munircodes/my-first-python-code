from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
search_terms = ["Python tutorial", "Selenium automation", "GitHub basics", "VS Code shortcuts"]
service = Service("C:/Users/huria/My git projects/my-first-python-code/chromedriver.exe")
driver = webdriver.Chrome(service=service)

for term in search_terms:
    driver.get("https://www.google.com")
    time.sleep(2)  # Let page load

    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()

    # Type slowly like a human
    for char in term:
        search_box.send_keys(char)
        time.sleep(0.2)  # 200ms delay between characters

    search_box.send_keys(Keys.RETURN)

    try:
        # Wait until results are visible (e.g. result stats or result links)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        print(f"✅ Search results loaded for: {term}")
    except:
        print(f"⚠️ Timed out waiting for results of: {term}")

    time.sleep(2)  # small pause before next search

# End
driver.quit()
