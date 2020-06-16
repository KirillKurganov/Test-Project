from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url=self.browser.current_url
        assert 'login' in url, 'URL NOT CORRECT'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register Form is not presented'

    def register_new_user(self,email,password):
        page=self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        page.click()
        post=self.browser.find_element(*LoginPageLocators.EMAIL)
        post.send_keys(email)
        login_password=self.browser.find_element(*LoginPageLocators.PASSWORD1)
        login_password.send_keys(password)
        login_password2=self.browser.find_element(*LoginPageLocators.PASSWORD2)
        login_password2.send_keys(password)
        button=self.browser.find_element(*LoginPageLocators.BUTTON_FOR_REGISTER)
        button.click()



