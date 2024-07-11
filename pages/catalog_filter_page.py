import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CatalogFilter(Base):

    # Локаторы - перечисляем локаторы на странице сайта

    product_locator = "(//div[@data-meta-product-id='1897350'])[1]"
    count_of_products = "//span[@data-meta-name='SubcategoryPageTitle__product-count']"
    price_filter = "(//div[@class='rc-slider-handle rc-slider-handle-2'])[3]"
    brand = "//input[@id='playstation']"

    # Поиск по локаторам с использованием явного ожидания и возврат результата поиска

    def get_product_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_locator)))

    def get_count_of_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.count_of_products)))

    def get_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter)))

    def get_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    # Действия - указываем, что именно будем делать с нашими локаторами

    def click_product_locator(self):
        self.get_product_locator()
        print("Click Product")

    def show_count_of_products(self):
        self.get_count_of_products()
        count = self.get_count_of_products().text.split()[0]
        print(f"Click Count Of Products = {count}")
        return count

    def click_price_filter(self):
        self.get_price_filter().click()
        action = ActionChains(self.driver)
        action.move_to_element(self.get_price_filter()).perform()
        action.click_and_hold(self.get_price_filter()).move_by_offset(-30, 0).release()
        action.perform()
        print("Apply Price Filter")

    def click_brand(self):
        media_filter = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@data-meta-value='Бренд']")))
        ActionChains(self.driver).move_to_element(media_filter).perform()
        self.driver.execute_script("window.scroll(0, 950)")
        self.get_brand().click() ##### НЕ НАЖИМАЕТСЯ ЧЕК-БОКС БРЕНД ######
        print("Click Brand Box")

    # Методы - вызываем в тестах

    def card_product(self):
        self.get_current_url()
        self.click_product_locator()

    def select_filter(self):
        count_prod = list()
        count_prod.append(self.show_count_of_products())
        time.sleep(5)
        self.click_price_filter()
        count_prod.append(self.show_count_of_products()) # Выводим кол-во товара после применения фильтра по цене
        time.sleep(5)
        self.click_brand()
        count_prod.append(self.show_count_of_products()) # Выводим кол-во товара после применения фильтра по бренду
        return count_prod