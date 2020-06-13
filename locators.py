from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM=(By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BASKET=(By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME=(By.CSS_SELECTOR, 'div.product_main h1')
    PRICE_BASKET=(By.CSS_SELECTOR,'.alert-info .alertinner strong')
    PRICE_PRODUCT=(By.CSS_SELECTOR,'.product_main .price_color')
    MESSAGE=(By.CSS_SELECTOR,'div.alertinner')


