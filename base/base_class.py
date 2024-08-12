import datetime
class Base():
    def __init__(self, driver): # Создали метод, который хранит наш драйвер
        self.driver = driver

    """Метод, сохраняющий скриншот страницы финиша"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        self.driver.save_screenshot((f'.\\screen\\screenshot{now_date}.png'))