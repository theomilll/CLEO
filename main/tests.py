from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
class cleo(TestCase):
    def test(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(r"C:\Users\caiob\OneDrive\Área de Trabalho\driver chrome\chromedriver.exe", options=chrome_options)

        driver.get("http://127.0.0.1:8000/")

        register = driver.find_element_by_id("signUp")
        register.click()
        username_register = driver.find_element_by_name("username_r")
        username_register.click()
        username_register.send_keys("thanos")
        email_register = driver.find_element_by_name("email_r")
        email_register.click()
        email_register.send_keys("thanos@gmail.com")
        password_register = driver.find_element_by_name("password1_r")
        password_register.click()
        password_register.send_keys("inevitavel40")
        confirm_register = driver.find_element_by_name("password2_r")
        confirm_register.click()
        confirm_register.send_keys("inevitavel40")

        botao_registrar = driver.find_element(By.XPATH, '//button[text()="Sign Up"]')
        botao_registrar.click()

        login = driver.find_element_by_id("signIn")
        driver.execute_script("arguments[0].click();", login)

        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("thanos")
        password.send_keys("inevitavel40")

        botao_login = driver.find_element(By.XPATH, '//button[text()="Log In"]')
        botao_login.click()

        adicionar_carrinho = driver.find_element_by_name("Adicionar ao carrinho")
        adicionar_carrinho.click()

        driver.quit()
