from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.catalog_filter_page import CatalogFilter
from pages.order_page import OrderPage
from pages.product_page import CardProductPage
from pages.registration_page import RegistrationPage


def smoke_test_f(get_driver):
    lp = Login_page(get_driver)
    lp.authorization()
    authorization_url = "https://www.citilink.ru/?_action=login&_success_login=1"
    assert lp.get_current_url() == authorization_url
    print("Good! You're authorization!")

    mp = Main_page(get_driver)
    mp.select_catalog()
    catalog_url = "https://www.citilink.ru/catalog/pristavki-playstation/"
    assert mp.get_current_url() == catalog_url
    print("Good! You're on catalog page!")

    cfp = CatalogFilter(get_driver)
    cfp.card_product()
    card_product_url = "https://www.citilink.ru/product/igrovaya-konsol-playstation-5-kabel-pitaniya-evrovilka-cfi-1200a-825gb-1897350/"
    assert cfp.get_current_url() == card_product_url
    print("Good! You're on catalog filter page!")

    pp = CardProductPage(get_driver)
    pp.go_to_cart()
    cart_url = "https://www.citilink.ru/order/"
    assert pp.get_current_url() == cart_url
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