import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options

fp = webdriver.FirefoxProfile('/root/.mozilla/firefox/i7qa87yy.default-esr')
wd = webdriver.Firefox(fp)
wd.get("https://colab.research.google.com/github/batata01/999/blob/main/zon3%20(4).ipynb")
print(wd.title)  
print("Page loaded")

wd.implicitly_wait(10)
wd.find_element_by_id('runtime-menu-button').click()
wd.find_element_by_id(':1w').click()

print("Running colab...")
print("Waiting for task to complete...")

while not os.path.isfile('/root/work/colabscript/Downloads/copy.txt'):
    time.sleep(1)

print("Task completed")

time.sleep(5)

print("Closing Driver...")

wd.quit()
