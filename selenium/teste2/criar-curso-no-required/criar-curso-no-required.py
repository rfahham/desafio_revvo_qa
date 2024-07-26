from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

# Acesso a Curso de Moodle

sleep(1)
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
sleep(1)

# Acessar página My Courses

navegador.get('https://sandbox.moodledemo.net/')
sleep(1)
navegador.find_elements(By.TAG_NAME, 'li')[2].click()
sleep(1)

# Acessar Create Course

navegador.get('https://sandbox.moodledemo.net/my/courses.php')
sleep(1)
navegador.find_elements(By.TAG_NAME, 'button')[5].click
sleep(1)

# Add a new course

navegador.get('https://sandbox.moodledemo.net/course/edit.php')

navegador.find_element('xpath', '//*[@id="id_saveanddisplay"]').click()
sleep(10)

# Fechando o navegador

navegador.quit()