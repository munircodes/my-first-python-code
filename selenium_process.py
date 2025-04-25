import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth

# --- Setup ChromeDriver and options ---
service = Service("C:/Users/huria/My git projects/my-first-python-code/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/huria/AppData/Local/Google/Chrome/User Data")  # your profile

# --- Launch browser ---
driver = webdriver.Chrome(service=service, options=options)

# --- Enable stealth mode ---
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)

# --- List of search terms ---
search_terms = ["Python tutorial", "Selenium automation", "GitHub basics", "VS Code tips"]

# --- Function to simulate human typing ---
def type_like_human(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(0.2)  # simulate human typing speed

# --- Loop through search terms ---
for term in search_terms:
    driver.get("https://www.google.com")
    
    time.sleep(2)  # give time to load
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()

    type_like_human(search_box, term)  # slow typing
    
    search_box.send_keys(Keys.RETURN)

    # ✅ Wait until search results appear before moving on
    time.sleep(5)  # you can increase if your internet is slow

# --- Keep browser open ---
input("✅ All searches done. Press Enter to close browser...")
driver.quit()
