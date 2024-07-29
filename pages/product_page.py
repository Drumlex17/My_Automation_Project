import code
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CardProductPage(Base):

    # Локаторы - перечисляем локаторы на странице сайта

    code_product = "//span[@class='e1n0yuko0 e1o6fkkp0 e106ikdt0 app-catalog-ahcgzg e1gjr6xo0']"
    button_cart = "//button[@data-meta-name='BasketDesktopButton']"
    go_cart_page = "(//span[@class='en3k2720 e106ikdt0 css-1y9ljh1 e1gjr6xo0'])[4]"

    # Поиск по локаторам с использованием явного ожидания и возврат результата поиска

    def get_code_product(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.code_product)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_go_cart_page(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.go_cart_page)))

    # Действия - указываем, что именно будем делать с нашими локаторами

    def show_code_product(self):
        self.get_code_product()
        self.code = self.get_code_product().text.split()[2]
        print(f"Code Product {self.code}")

    def click_button_cart(self):
        self.get_button_cart().click()
        print("Click Button Cart")

    def click_go_cart_page(self):
        self.get_go_cart_page().click()
        print("Click Cart Page")

    # Методы - вызываем в тестах

    def go_to_cart(self):
        self.show_code_product()
        self.click_button_cart()
        self.click_go_cart_page()