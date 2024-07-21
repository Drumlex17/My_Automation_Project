from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.catalog_filter_page import CatalogFilter
from pages.order_page import OrderPage
from pages.product_page import CardProductPage
from pages.registration_page import RegistrationPage


def smoke_test_f(get_driver):
    lp = Login_page(get_driver)
    lp.authorization()
    print("Good! You're authorization!")

    mp = Main_page(get_driver)
    mp.select_catalog()
    catalog_url = "https://www.citilink.ru/catalog/pristavki-playstation/"
    print("Good! You're on catalog page!")

    cfp = CatalogFilter(get_driver)
    cfp.select_filter()
    cfp.card_product()
    print("Good! You're on catalog filter page!")

    pp = CardProductPage(get_driver)
    pp.go_to_cart()
    print("Good! You're on cart page!")

    rp = RegistrationPage(get_driver)
    rp.go_to_registration()
    assert pp.code == rp.code
    print("Product code matches!")
    print("Good! You're on registration page!")

    op = OrderPage(get_driver)
    op.end_registration()
    assert op.get_approved_order() == 'Заказ ожидает оплаты!' or 'Заказ резервируется!'
    op.get_screenshot()
    print('Good! Smoke Testing End!')