from selenium import webdriver

#Manter a versão do webdriver atualizar
from webdriver_manager.chrome import ChromeDriverManager

# Interações com o navegador
from selenium.webdriver.chrome.service import Service
import time


# Webdriver atualizado
service = Service(ChromeDriverManager().install())

#Configurando meu navegador
navegador = webdriver.Chrome(service=service)

#Abrindo a URL
url= r'https://forms.gle/mqdM3UdN1mFtpFXs7'
navegador.get(url=url)

time.sleep(5)

navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Thiago')

time.sleep(2)

navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('teste@hotmail.com')

time.sleep(2)

navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys('av do teste, 515')

time.sleep(2)

navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('85999999999')

time.sleep(2)

navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click ()

time.sleep(5)