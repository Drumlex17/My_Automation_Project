import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CatalogFilter(Base):

    # Локаторы - перечисляем локаторы на странице сайта

    product_locator = "(//div[@data-meta-product-id='1897350'])[1]"
    count_of_products = "//span[@data-meta-name='SubcategoryPageTitle__product-count']"
    price_filter_min = "(//input[@data-meta-name='FilterRangeGroup__input-min'])[2]"
    price_filter_max = "(//input[@data-meta-name='FilterRangeGroup__input-max'])[2]"
    brand = "//span[text()='PLAYSTATION']"
    go_product_page = "(//a[@href='/product/igrovaya-konsol-playstation-5-kabel-pitaniya-evrovilka-cfi-1200a-825gb-1897350/'])[3]"

    # Поиск по локаторам с использованием явного ожидания и возврат результата поиска

    def get_product_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_locator)))

    def get_count_of_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.count_of_products)))

    def get_price_filter_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter_min)))

    def get_price_filter_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter_max)))

    def get_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    def get_go_product_page(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.go_product_page)))

    # Действия - указываем, что именно будем делать с нашими локаторами

    def click_product_locator(self):
        self.get_product_locator()
        print("Click Product")

    def show_count_of_products(self):
        self.get_count_of_products()
        count = self.get_count_of_products().text.split()[0]
        print(f"Click Count Of Products = {count}")
        return count

    def click_price_filter_min(self):
        self.get_price_filter_min().clear()
        self.get_price_filter_min().send_keys('50000')
        self.get_price_filter_min().send_keys(Keys.ENTER)
        print("Apply Price Filter Min")

    def click_price_filter_max(self):
        self.get_price_filter_max().clear()
        self.get_price_filter_max().send_keys('69000')
        self.get_price_filter_max().send_keys(Keys.ENTER)
        print("Apply Price Filter Max")

    def click_brand(self):
        media_filter = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@data-meta-value='Бренд']")))
        ActionChains(self.driver).move_to_element(media_filter).perform()
        self.get_brand().click()
        print("Click Brand Box")

    def click_go_product_page(self):
        self.get_go_product_page().click()
        print("Click Product Page")

    # Методы - вызываем в тестах

    def card_product(self):
        self.get_current_url()
        self.click_product_locator()

    def select_filter(self):
        count_prod = list()
        count_prod.append(self.show_count_of_products())
        time.sleep(5)
        self.click_price_filter_min() # Выводим минимальное кол-во товара после применения фильтра по цене
        count_prod.append(self.show_count_of_products())
        self.click_price_filter_max()
        count_prod.append(self.show_count_of_products()) # Выводим максимальное кол-во товара после применения фильтра по цене
        time.sleep(5)
        self.driver.execute_script("window.scroll(0, 950)")
        self.click_brand()
        count_prod.append(self.show_count_of_products()) # Выводим кол-во товара после применения фильтра по бренду
        time.sleep(5)
        self.driver.execute_script("window.scroll(0, 0)")
        self.click_go_product_page()
        return count_prod