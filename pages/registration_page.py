from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class RegistrationPage(Base):

    # Локаторы - перечисляем локаторы на странице сайта

    code_product = "//span[contains(text(), 'Код товара')]"
    button_registration = "//button[@class='e4uhfkv0 css-ki69qx e4mggex0']"

    # Поиск по локаторам с использованием явного ожидания и возврат результата поиска

    def get_code_product(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.code_product)))

    def get_button_registration(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_registration)))

    # Действия - указываем, что именно будем делать с нашими локаторами

    def show_code_product(self):
        self.get_code_product()
        self.code = self.get_code_product().text.split()[2]
        print(f"Code Product {self.code}")

    def click_button_registration(self):
        self.get_button_registration().click()
        print("Click Button Registration")

    # Методы - вызываем в тестах

    def go_to_registration(self):
        self.show_code_product()
        self.click_button_registration()