import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth

# Setup ChromeDriver
service = Service("C:/Users/huria/My git projects/my-first-python-code/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Stealth settings to reduce bot detection
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# Search terms list
search_terms = ["Python tutorial", "Selenium automation", "GitHub basics", "VS Code shortcuts"]

# --- Function to simulate human typing ---
def type_like_human(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(0.2)  # simulate human typing speed


# Prepare results list
results = []

for term in search_terms:
    driver.get("https://www.google.com")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()

    type_like_human(search_box, term)  # slow typing
   
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    try:
        # Find first search result
        first_result = driver.find_element(By.CSS_SELECTOR, 'div#search a')
        title = first_result.text
        url = first_result.get_attribute("href")

        results.append({
            "Search Term": term,
            "Title": title,
            "URL": url
        })
    except Exception as e:
        results.append({
            "Search Term": term,
            "Title": "No result found",
            "URL": "N/A"
        })
        print(f"Error for '{term}': {e}")

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("google_search_results.csv", index=False)
print("✅ Search results saved to 'google_search_results.csv'")

# Keep browser open
input("Press Enter to close the browser...")
driver.quit()
