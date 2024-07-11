#### Создание класса страницы Авторизации. Взаимодействие с модулем test_buy_product ###


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):

    # Локаторы - перечисляем локаторы на странице сайта

    log_in = "(//div[@class='css-1wyvf5z eyoh4ac0'])[1]"
    email = "//input[@name='login']"
    password = "//input[@name='pass']"
    login_button = "//button[@class='e4uhfkv0 css-1nvnwij e4mggex0']"

    # Поиск по локаторам с использованием явного ожидания и возврат результата поиска

    def get_log_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.log_in)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Действия - указываем, что именно будем делать с нашими локаторами

    def click_log_in(self):
        self.get_log_in().click()
        print("Click Log In")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input Email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login Button")

    # Методы - вызываем в тестах

    def authorization(self):
        self.get_current_url()
        self.click_log_in()
        self.input_email("wefare9126@nolanzip.com")
        self.input_password("TestQATest")
        self.click_login_button()