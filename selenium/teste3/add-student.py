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

# Selecionar o curso

navegador.get('https://sandbox.moodledemo.net/')

navegador.find_element('xpath', '//*[@id="frontpage-available-course-list"]/div/div[2]/div[1]/h3/a').click()
sleep(1)

# Adicionar estudante ao curso

navegador.get('https://sandbox.moodledemo.net/course/view.php?id=3')

# Botão participantes

navegador.find_elements(By.TAG_NAME, 'li')[8].text
sleep(2)
navegador.find_elements(By.TAG_NAME, 'li')[8].click()
sleep(2)
# Redireciona para a página de user

navegador.get('https://sandbox.moodledemo.net/user/index.php?id=3')

navegador.find_element('xpath', '//*[@id="enrolusersbutton-1"]/div/input[1]').click()

# Enrolment options
navegador.find_elements(By.TAG_NAME, 'li')[1].text
navegador.find_elements(By.TAG_NAME, 'div')[1].text

# navegador.find_element('xpath', '//*[@id="form_autocomplete_input-1722177886105"]').text

