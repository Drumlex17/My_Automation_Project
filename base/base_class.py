#### Модуль связан с модулями login_page и test_buy_product ###


import datetime
class Base():
    def __init__(self, driver): # Создали метод, который хранит наш драйвер
        self.driver = driver

    """Метод отображающий текущий URL"""

    def get_current_url(self):
        get_url = self.driver.current_url # В данном случае current_url это встроенная функция самого Python, поэтому с помощью неё можно отслеживать текущий URL
        print(f'Current URL: {get_url}')

    """Метод, сохраняющий скриншот страницы финиша"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        self.driver.save_screenshot((f'.\\screen\\screenshot{now_date}.png'))