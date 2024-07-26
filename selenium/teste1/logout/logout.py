# pip install selenium 
# pip install webdriver-manager 

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

# Login

sleep(10)
navegador.get('https://sandbox.moodledemo.net/login/index.php')
sleep(1)
navegador.find_element('xpath', '//*[@id="username"]').send_keys('admin')
sleep(1)
navegador.find_element('xpath', '//*[@id="password"]').send_keys('sandbox')
sleep(1)
navegador.find_element('xpath', '//*[@id="loginbtn"]').click()
sleep(10)

# Logout

navegador.find_element('xpath', '//*[@id="user-menu-toggle"]').click()
sleep(1)
navegador.find_element('xpath', '//*[@id="carousel-item-main"]/a[10]').click()
sleep(1)