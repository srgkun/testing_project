from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, \
            "The sub-line 'login' isn't in URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def should_be_success_message(self):
        print("уведомление об успехе регистрации")
        assert self.is_element_present(*LoginPageLocators.SUCCESS_MESSAGE), \
            "Registration is nor success"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FORM)
        email_form.send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FORM)
        password_form.send_keys(password)
        password_form_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FORM_CONFIRM)
        password_form_confirm.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()