import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(options=options)

# Navigáljunk a Chrome új fül oldalára
driver.get('https://kivy.org/doc/stable/#')

# Találjuk meg a Képek gombot és kattintsunk rá
images_button = driver.find_element('xpath','//*[@id="contentall"]/div[1]/div/ul[2]/li[4]/a' )
images_button.click()

# Írjunk ki egy üzenetet, majd várjunk 10 másodpercet.
print("Nyisson meg egy képet a böngészőben.")
time.sleep(10)

# Ne zárjuk be a böngészőt, ha végeztünk
driver.quit()
