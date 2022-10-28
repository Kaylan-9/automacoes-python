from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from threading import Thread
from webdriver_manager.chrome import ChromeDriverManager

class EcommerceBot():
    def __init__(self, segundo_plano=False):
        options = Options()
        if segundo_plano:
            options.add_argument("--headless")
        website = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"
        self.driver =  webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get(website)

    def escreve_nome(self, nome):
        primeiro_nome = self.driver.find_element(By.ID, 'input-firstname')
        primeiro_nome.send_keys(nome)
    
    def escreve_sobrenome(self, sobrenome):
        ultimo_nome = self.driver.find_element(By.ID, "input_lastname")
        ultimo_nome.send_keys(sobrenome)

    def escreve_email(self, email):
        user_email = self.driver.find_element(By.XPath, '//*[@id="input-email"]')
        user_email.send_keys(email)

    def escreve_telefone(self, telefone):
        user_telefone = self.driver.find_element(By.CLASS_NAME, 'cold-sm_10')
        user_telefone.send_keys(telefone)