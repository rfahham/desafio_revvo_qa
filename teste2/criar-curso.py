# pip install selenium 
# pip install webdriver-manager 

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

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

## Criar Curso

# navegador.get('https://sandbox.moodledemo.net/my/courses.php')
# sleep(60)

navegador.find_element('xpath', '//*[@id="moremenu-66a2b9b459240-navbar-nav"]/li[3]/a').click()
sleep(60)




# navegador.find_element('xpath', '//*[@id="single_button66a2b98caa3481"]').click()
# sleep(1)

# Add a new course
# navegador.get('https://sandbox.moodledemo.net/course/edit.php')
# sleep(1)

# Course full name
# navegador.find_element('xpath', '//*[@id="id_fullname"]').send_keys('Curso de Selenium')
# sleep(1)

# Course short name
# navegador.find_element('xpath', '//*[@id="id_shortname"]').send_keys('Selenium')

# Course start date
# navegador.find_element('xpath', '//*[@id="yui_3_18_1_1_1721939438641_767"]').click()
