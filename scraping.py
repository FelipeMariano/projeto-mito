import os
import time
from selenium import webdriver
import yaml
from datetime import date

cur_dir = os.path.dirname(os.path.realpath(__file__))
secret_path = os.path.join(cur_dir, 'secrets.yml')

with open(secret_path, 'r') as stream:
	data = yaml.load(stream)
	USERNAME = data.get('user', '')
	PASSWORD = data.get('password')

driver = webdriver.Firefox()
driver.get("https://login.globo.com/login/438?url=https://cartolafc.globo.com")
driver.maximize_window()

email = driver.find_element_by_id("login")
email.send_keys(USERNAME)
senha = driver.find_element_by_id("password")
senha.send_keys(PASSWORD)
driver.find_element_by_xpath("//*[@id='tpl-content']/div[2]/div[1]/form/div[7]/button").click()
time.sleep(10)
driver.get("https://cartolafc.globo.com/#/time")

lista_atletas = driver.find_elements_by_xpath('/html/body/div[1]/div[5]/ui-view/div[4]/div/div[3]/div')[0]
atletas = lista_atletas.find_elements_by_class_name('cartola-atletas__card')

print atletas[0].text

