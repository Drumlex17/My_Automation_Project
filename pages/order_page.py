from datetime import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class OrderPage(Base):

    # Локаторы - перечисляем локаторы на странице сайта

    customer_data = "//button[@class='e4uhfkv0 css-pjyyz3 e4mggex0']"
    first_name = "//input[@name='RecipientForm__first-name']"
    last_name = "//input[@name='RecipientForm__last-name']"
    phone_number = "(//input[@name='input-validation-field'])[1]"
    create_button = "//button[@class='e4uhfkv0 css-gh3izc e4mggex0']"
    production_method = "//button[@class='e4uhfkv0 css-1w7mt1x e4mggex0']"
    place_purchase = "//button[@class='e1tiqnd20 css-18kees1 e4mggex0']"
    confirm_data = "//span[contains(text(), 'Данные получателя указаны верно*')]"
    order = "//button[@class='e1jq023s0 css-ol7d38 e4mggex0']"
    approved_order = "//span[contains(text(), 'Заказ ожидает оплаты!')]"

    # Поиск по локаторам с использованием явного ожидания и возврат результата поиска

    def get_customer_data(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.customer_data)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_create_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.create_button)))

    def get_production_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.production_method)))

    def get_place_purchase(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.place_purchase)))

    def get_confirm_data(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_data)))

    def get_order(self):
        return self.driver.find_element(by=By.XPATH, value=self.order)

    def get_approved_order(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.approved_order))).text

    # Действия - указываем, что именно будем делать с нашими локаторами

    def click_customer_data(self):
        self.get_customer_data().click()
        print("Click Customer Data!")

    def click_first_name(self):
        self.get_first_name().send_keys("Ivan")
        print("First Name written!")

    def click_last_name(self):
        self.get_last_name().send_keys("Ivanov")
        print("Last Name written!")

    def click_phone_number(self):
        self.get_phone_number().send_keys('79600248889')
        print("Phone Number written!")

    def click_create_button(self):
        self.get_create_button().click()
        print("Click Create Button!")

    def click_production_method(self):
        self.get_production_method().click()
        print("Click Production Method!")

    def click_place_purchase(self):
        self.get_place_purchase().click()
        print("Click Place Purchase!")

    def click_confirm_data(self):
        self.get_confirm_data().click()
        print("Click Confirm Data!")

    def click_order(self):
        self.get_order().click()
        print("Click Order!")

    # Методы - вызываем в тестах

    def end_registration(self):
        self.click_customer_data()
        self.click_first_name()
        self.click_last_name()
        self.click_phone_number()
        self.click_create_button()
        self.click_production_method()
        self.click_place_purchase()
        self.click_confirm_data()
        self.click_order()