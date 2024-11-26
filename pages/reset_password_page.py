import allure
from pages.base_page import BasePage
from pages_locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    @allure.step("Клик на кнопку 'Глаз'")
    def click_on_eye_button(self):
        eye_button = self.find_element_with_wait(ResetPasswordPageLocators.EYE_BUTTON)
        self.click_on_element_js(eye_button)

    @allure.step("Проверка видимости пароля")
    def is_password_visible(self):
        password_input = self.find_element_with_wait(ResetPasswordPageLocators.RESET_PASSWORD_INPUT)
        return password_input.get_attribute('type') == 'text'
