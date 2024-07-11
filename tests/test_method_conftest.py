from pages.catalog_filter_page import CatalogFilter
from pages.main_page import Main_page
from pages.login_page import Login_page



def test_method_conftest(set_up, get_driver):
    lp = Login_page(get_driver)
    lp.authorization()

    mp = Main_page(get_driver)
    mp.select_catalog()

    cp = CatalogFilter(get_driver)
    count = cp.select_filter()
    print(f'Count Products: {count}')
    cp.get_screenshot()
    print("Test Method Conftest End!")