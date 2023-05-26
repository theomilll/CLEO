from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .forms import SignUpForm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class cleo(TestCase):
    def test(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get("http://127.0.0.1:8000/")

        self.run_tests(driver)

    def register(self, driver):
        register = driver.find_element(By.ID,"signUp")
        register.click()
        time.sleep(2)
        username_register = driver.find_element(By.NAME,"username")
        username_register.send_keys("thanos")
        email_register = driver.find_element(By.NAME,"email")
        email_register.send_keys("thanos@gmail.com")
        password_register = driver.find_element(By.NAME,"password1")
        password_register.send_keys("inevitavel40")
        confirm_register = driver.find_element(By.NAME,"password2")
        confirm_register.send_keys("inevitavel40")
        login = driver.find_element(By.ID,"Sign Up")
        login.click()
    def login(self, driver):
        escrever_username = driver.find_element(By.NAME,"Username")
        escrever_username.send_keys("thanos")
        password_login = driver.find_element(By.NAME,"password")
        password_login.send_keys("inevitavel40")
        botao_login = driver.find_element(By.NAME,"login")
        botao_login.click()
    def status_pedido(self, driver):
        view_order_status = driver.find_element(By.ID,'sino')
        view_order_status.click()
        time.sleep(2)
        backtocatalog1 = driver.find_element(By.ID,'arrow')
        backtocatalog1.click()
    def busca_produto_existente(self, driver):
        busca = driver.find_element(By.NAME,"search")
        busca.send_keys("pastel")
        btn_busca = driver.find_element(By.ID,"btn-busca")        
        btn_busca.click()
        busca = driver.find_element(By.NAME,"search")
        busca.clear()
        btn_busca = driver.find_element(By.ID,"btn-busca")
        btn_busca.click()
    def busca_produto_inexistente(self, driver):
        busca = driver.find_element(By.NAME,"search")
        busca.send_keys("lasanha")
        btn_busca = driver.find_element(By.ID,"btn-busca")
        btn_busca.click()
        busca = driver.find_element(By.NAME,"search")
        busca.clear()
        btn_busca = driver.find_element(By.ID,"btn-busca")
        btn_busca.click()
    def adicionarcarrinho(self, driver):
        adicionar_carrinho = driver.find_element(By.NAME,"cartAdd")
        adicionar_carrinho.click()
    def detalhes_produto(self, driver):
        first_product = driver.find_element(By.NAME, "product-link")
        first_product.click()
        for i in range(4):
            increase_button = driver.find_element(By.NAME, "increase")
            increase_button.click()
        for i in range(4):
            decrease_button = driver.find_element(By.NAME, "decrease")
            decrease_button.click()
        adicionar_carrinho2 = driver.find_element(By.NAME, "cartAdd")
        adicionar_carrinho2.click()
        time.sleep(2)
    def entrar_carrinho(self, driver):
        cartBtn = driver.find_element(By.NAME, "cart")
        cartBtn.click()
    def alterar_quantidade(self, driver):
        for i in range(2):
            cartDecrease = driver.find_element(By.NAME, "decreaseCart")
            cartDecrease.click()
        for i in range(2):
            cartIncrease = driver.find_element(By.NAME, "increaseCart")
            cartIncrease.click()
    def adicionar_obs(self, driver):
        cartObs = driver.find_element(By.NAME, "text_box_obs")
        cartObs.send_keys("Eu sou inevitavel!")
        cartObsBtn = driver.find_element(By.NAME, "obsCartBtn")
        cartObsBtn.click()
    def finalizar_compra(self, driver):
        finalizarCompra = driver.find_element(By.NAME, "finalizarCompra")
        finalizarCompra.click()
    def metodo_pagamento(self, driver):
        paymentMethod = driver.find_element(By.NAME, 'payment-method')
        paymentMethod.click()
        pixPay = driver.find_element(By.NAME, "pixPay")
        pixPay.click()
        qrCodeGen = driver.find_element(By.NAME, "generateQrCode")
        qrCodeGen.click()
    def confirmar_compra(self, driver):
        selecionar_tempo = driver.find_element(By.NAME, "pickup-time")
        selecionar_tempo.send_keys("1030")
        time.sleep(2)
        confirmPurchase = driver.find_element(By.NAME, "generateQrCode")
        confirmPurchase.click()
        time.sleep(2)
    def finalizar_pedido(self, driver):
        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "confirmPurchase")))
        FinalizarPedido=driver.find_element(By.ID, "confirmPurchase")
        FinalizarPedido.click()
    def voltar_catalogo(self, driver):
        voltar_catalogo=driver.find_element(By.ID, "arrow")
        voltar_catalogo.click()
    def logout(self, driver):
        logout= driver.find_element(By.ID,"log-out")
        logout.click()
    def pagamento_cartao(self, driver):
        escrever_username1 = driver.find_element(By.NAME,"Username")
        escrever_username1.send_keys("thanos")
        password_login1 = driver.find_element(By.NAME,"password")
        password_login1.send_keys("inevitavel40")
        botao_login1 = driver.find_element(By.NAME,"login")
        botao_login1.click()
        adicionar_carrinho1 = driver.find_element(By.NAME,"cartAdd")
        adicionar_carrinho1.click()
        cartBtn1 = driver.find_element(By.NAME, "cart")
        cartBtn1.click()
        finalizarCompra1 = driver.find_element(By.NAME, "finalizarCompra")
        finalizarCompra1.click()
        paymentMethod1 = driver.find_element(By.NAME, 'payment-method')
        paymentMethod1.click()
        cartao_credito1 = driver.find_element(By.NAME, "Cartao-credito")
        cartao_credito1.click()
        selecionar_tempo1 = driver.find_element(By.NAME, "pickup-time")
        selecionar_tempo1.send_keys("1030")
        confirmPurchase1 = driver.find_element(By.NAME, "generateQrCode")
        confirmPurchase1.click()
        nome_cartao = driver.find_element(By.NAME,"name")
        nome_cartao.send_keys("Thor")
        numero_cartao = driver.find_element(By.NAME,"card_number")
        numero_cartao.send_keys("4111111111111111")
        data_expediçao = driver.find_element(By.NAME,"expiry_date")
        data_expediçao.send_keys("13062023")
        data_expediçao = driver.find_element(By.NAME,"cvv_code")
        data_expediçao.send_keys("666")
        confirmar_cartao = driver.find_element(By.NAME, "btn-confirmar")
        confirmar_cartao.click()
        voltar_catalogo1=driver.find_element(By.ID, "arrow")
        voltar_catalogo1.click()
        logout1= driver.find_element(By.ID,"log-out")
        logout1.click()
        driver.quit()
    def run_tests(self, driver):
        self.register(driver)
        self.login(driver)
        self.status_pedido(driver)
        self.busca_produto_existente(driver)
        self.busca_produto_inexistente(driver)
        self.adicionarcarrinho(driver)
        self.detalhes_produto(driver)
        self.entrar_carrinho(driver)
        self.alterar_quantidade(driver)
        self.adicionar_obs(driver)
        self.finalizar_compra(driver)
        self.metodo_pagamento(driver)
        self.confirmar_compra(driver)
        self.finalizar_pedido(driver)
        self.voltar_catalogo(driver)
        self.logout(driver)
        self.pagamento_cartao(driver)