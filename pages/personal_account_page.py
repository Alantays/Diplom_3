import allure
from pages.base_page import BasePage
from pages_locators.personal_account_page_locators import PersonalAccountPageLocators
from pages_locators.main_page_locators import MainPageLocators


class PersonalAccountPage(BasePage):
    @allure.step("Клик нк кнооку 'История заказов'")
    def click_on_order_history_button(self, url):
        order_history = self.find_element_with_wait(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element_js(order_history)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Выход из личного кабинета")
    def logout(self, url):
        logout_button = self.find_element_with_wait(PersonalAccountPageLocators.LOGOUT_BUTTON)
        self.click_on_element_js(logout_button)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Нажатие на кнопку 'Лента заказов'")
    def click_on_order_feed_button(self, url):
        order_feed_button = self.find_element_with_wait(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element_js(order_feed_button)
        self.wait_for_url_to_be(url)

    @allure.step("Получение номера заказа из истории заказов")
    def get_order_number_from_orders_history(self):
        self.find_element_with_wait(PersonalAccountPageLocators.LAST_ORDER_NUMBER)
        order_number = self.get_text_from_element(PersonalAccountPageLocators.LAST_ORDER_NUMBER)
        return order_number
