from pages.base_page import BasePage
from pages_locators.order_feed_page_locators import OrderFeedPageLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure


class OrderFeedPage(BasePage):

    @allure.step("Клик на кнопку 'Конструктор'")
    def click_on_constructor_button(self, url):
        constructor_button = self.find_element_with_wait(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element_js(constructor_button)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Клик на заказ")
    def click_on_order(self):
        order = self.find_element_with_wait(OrderFeedPageLocators.ORDER)
        self.click_on_element_js(order)

    @allure.step("Проверка видимости окна деталей заказа")
    def order_details_window_is_visible(self):
        order_details_window = self.find_element_with_wait(OrderFeedPageLocators.ORDER_DETAILS_WINDOW)
        return order_details_window.is_displayed()

    @allure.step("Проверка наличия номера заказа в списке всех заказов")
    def is_order_number_in_list(self, order_number):
        order_elements = self.find_elements_with_wait(OrderFeedPageLocators.ORDER_LIST)

        for _ in order_elements:
            order_number_text = self.get_text_from_element(OrderFeedPageLocators.ORDER_LIST_NUMBERS)
            if order_number_text == order_number:
                return True
        return False

    @allure.step("Получение номера счетчика выполненных заказов за все время")
    def get_all_time_counter_number(self):
        self.find_element_with_wait(OrderFeedPageLocators.ALL_TIME_COUNTER)
        all_time_counter = self.get_text_from_element(OrderFeedPageLocators.ALL_TIME_COUNTER)
        return all_time_counter

    @allure.step("Проверка увеличения счетчика выполненных заказов за все время")
    def is_all_time_counter_increased(self, initial_counter):
        current_counter = self.get_all_time_counter_number()
        return int(current_counter) > int(initial_counter)

    @allure.step("Получение номера счетчика выполненных заказов за сегодня")
    def get_today_counter_number(self):
        self.find_element_with_wait(OrderFeedPageLocators.TODAY_COUNTER)
        today_counter = self.get_text_from_element(OrderFeedPageLocators.TODAY_COUNTER)
        return today_counter

    @allure.step("Проверка увеличения счетчика выполненных заказов за сегодня")
    def is_today_counter_increased(self, initial_counter):
        current_counter = self.get_today_counter_number()
        return int(current_counter) > int(initial_counter)

    @allure.step("Ожидание появления заказа в списке заказов 'В работе'")
    def wait_for_order_to_appear(self, order_number):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.is_order_number_in_work_list(order_number)
        )
        return True

    @allure.step("Проверка наличия номера заказа в списке 'В работе'")
    def is_order_number_in_work_list(self, order_number):
        orders_section = self.find_elements_with_wait(OrderFeedPageLocators.IN_WORK_ORDERS)

        for order in orders_section:
            order_text = order.text[1:]
            if order_text == order_number:
                return True
        return False
