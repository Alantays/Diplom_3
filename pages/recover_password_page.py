import allure
from pages.base_page import BasePage
from pages_locators.recover_password_page_locators import RecoverPasswordPageLocators


class RecoverPasswordPage(BasePage):

    @allure.step("Ввод email")
    def input_email(self, email):
        self.find_element_with_wait(RecoverPasswordPageLocators.EMAIL_INPUT)
        self.add_text_to_element(RecoverPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step("Клик на кнопку 'Восстановить'")
    def click_on_recover_button(self, url):
        recover_button = self.find_element_with_wait(RecoverPasswordPageLocators.RECOVER_BUTTON)
        self.click_on_element_js(recover_button)
        self.wait_for_url_to_be(url)
        return self.get_current_url()
