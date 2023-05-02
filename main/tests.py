from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .forms import SignUpForm
class cleo(TestCase):
    def test(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(r"C:\Users\caiob\OneDrive\Área de Trabalho\driver chrome\chromedriver.exe", options=chrome_options)

        driver.get("http://127.0.0.1:8000/")
        register = driver.find_element(By.ID,"signUp")
        register.click()
        time.sleep(2)
        username_register = driver.find_element(By.NAME,"username")
        username_register.send_keys("thanos")
        time.sleep(1)
        email_register = driver.find_element(By.NAME,"email")
        email_register.send_keys("thanos@gmail.com")
        time.sleep(1)
        password_register = driver.find_element(By.NAME,"password1")
        password_register.send_keys("inevitavel40")
        time.sleep(1)
        confirm_register = driver.find_element(By.NAME,"password2")
        confirm_register.send_keys("inevitavel40")
        time.sleep(1)
        login = driver.find_element(By.ID,"Sign Up")
        login.click()
        escrever_username = driver.find_element(By.NAME,"Username")
        escrever_username.send_keys("thanos")
        time.sleep(1)
        password_login = driver.find_element(By.NAME,"password")
        password_login.send_keys("inevitavel40")
        time.sleep(1)
        botao_login = driver.find_element(By.NAME,"login")
        botao_login.click()
        adicionar_carrinho = driver.find_element(By.NAME,"Adicionar ao carrinho")
        adicionar_carrinho.click()
        time.sleep(2)
        driver.quit()
