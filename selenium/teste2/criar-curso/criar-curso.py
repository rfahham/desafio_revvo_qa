# pip install selenium 
# pip install webdriver-manager 

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

## Login

# Acesso a Curso de Moodle

sleep(10)
navegador.get('https://sandbox.moodledemo.net/login/index.php')
sleep(1)
# Usuário
navegador.find_element('xpath', '//*[@id="username"]').send_keys('admin')
sleep(1)
# Senha
navegador.find_element('xpath', '//*[@id="password"]').send_keys('sandbox')
sleep(1)
# Botão de Acesso
navegador.find_element('xpath', '//*[@id="loginbtn"]').click()
sleep(10)

## Acessar página My Courses

navegador.get('https://sandbox.moodledemo.net/')
sleep(1)
navegador.find_elements(By.TAG_NAME, 'li')[2].click()
sleep(1)

## Acessar Create Course

navegador.get('https://sandbox.moodledemo.net/my/courses.php')
sleep(1)
navegador.find_elements(By.TAG_NAME, 'button')[5].click
sleep(1)

# Add a new course

navegador.get('https://sandbox.moodledemo.net/course/edit.php')

# Course full name
navegador.find_element('xpath', '//*[@id="id_fullname"]').send_keys('Curso de Selenium')
sleep(1)

# Course short name
navegador.find_element('xpath', '//*[@id="id_shortname"]').send_keys('Selenium')
sleep(1)

# Course start date

## Day
navegador.find_element('xpath', '//*[@id="id_startdate_day"]').send_keys('1')
sleep(1)

## Month
navegador.find_element('xpath', '//*[@id="id_startdate_month"]').send_keys('August')
sleep(1)

## Year
# navegador.find_element('xpath', '//*[@id="id_startdate_year"]').send_keys('2024')
# sleep(1)

# Course end date

## Day
navegador.find_element('xpath', '//*[@id="id_enddate_day"]').send_keys('31')
sleep(1)

## Month
navegador.find_element('xpath', '//*[@id="id_enddate_month"]').send_keys('August')
sleep(1)

## Year
# navegador.find_element('xpath', '//*[@id="id_endtdate_year"]').send_keys('2024')
# sleep(1)

# Description
# navegador.find_element('xpath', '//*[@id="tinymce"]/p')[1].send_keys('Selenium')
# navegador.find_elements(By.TAG_NAME, 'p')[1].text
# sleep(1)

navegador.find_element('xpath', '//*[@id="id_saveanddisplay"]').click()
sleep(10)

## Fechando o navegador

navegador.quit()