from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    # Локаторы - перечисляем локаторы на странице сайта

    main_word = "//span[@class='e1aqfeo90 e106ikdt0 app-catalog-1qazt9q e1gjr6xo0']"
    catalog = "//span[contains(text(), 'Каталог товаров')]"
    gamer = "(//a[@href='/catalog/tovary-dlya-geimerov/?ref=mainmenu'])[2]"
    playstation = "//a[contains(text(), 'Приставки PlayStation')]"

    # Поиск по локаторам с использованием явного ожидания и возврат результата поиска

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_gamer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gamer)))

    def get_link_playstation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.playstation)))

    # Действия - указываем, что именно будем делать с нашими локаторами

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def click_link_catalog(self):
        self.get_catalog().click()
        print("Click Catalog")

    def click_gamer(self):
        self.get_gamer().click()
        print("Click Category For Gamers")

    def click_link_playstation(self):
        self.get_link_playstation().click()
        print("Click Link Playstation")

    # Методы - вызываем в тестах

    def select_catalog(self):
        self.get_current_url()
        self.click_link_catalog()
        self.click_gamer()
        self.click_link_playstation()