from pages.base_page import BasePage
from pages_locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step("Клик на кнопку 'Войти в аккаунт'")
    def click_on_login_button(self):
        login_button = self.find_element_with_wait(MainPageLocators.LOGIN_BUTTON)
        self.click_on_element_js(login_button)

    def wait_page_to_be_loaded(self):
        self.find_element_with_wait(MainPageLocators.MAIN_PAGE_HEADER)

    @allure.step("Клик на кнопку 'Личный кабинет'")
    def click_on_personal_account_button(self, url):
        personal_account_button = self.find_element_with_wait(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element_js(personal_account_button)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Клик на кнопку 'Лента заказов'")
    def click_on_order_feed_button(self, url):
        order_feed_button = self.find_element_with_wait(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element_js(order_feed_button)
        self.wait_for_url_to_be(url)
        return self.get_current_url()

    @allure.step("Клик на ингредиент")
    def click_on_ingredient(self):
        ingredient = self.find_element_with_wait(MainPageLocators.INGREDIENT)
        self.click_on_element_js(ingredient)

    @allure.step("Проверка видимости окна деталей ингредиента")
    def ingredient_details_window_is_visible(self):
        ingredient_details_window = self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_WINDOW)
        return ingredient_details_window.is_displayed()

    @allure.step("Закрытие окна деталей ингредиента")
    def close_ingredient_details_window(self):
        close_button = self.find_element_with_wait(MainPageLocators.CLOSE_DETAILS_WINDOW_BUTTON)
        self.click_on_element_js(close_button)
        modal_element = self.find_element_with_wait(MainPageLocators.MODAL_ELEMENT)
        return 'Modal_modal_opened__3ISw4' not in modal_element.get_attribute('class')

    @allure.step("Перемещение ингредиента в корзину")
    def move_ingredient_to_order(self):
        source = self.find_element_with_wait(MainPageLocators.INGREDIENT)
        target = self.find_element_with_wait(MainPageLocators.BASKET)
        self.move_elements(source, target)

    @allure.step("Проверка увеличения счетчика ингредиента")
    def is_ingredient_counter_increased(self):
        self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER)
        counter_text = self.get_text_from_element(MainPageLocators.INGREDIENT)
        return counter_text != '0'

    @allure.step("Клик на кнопку 'Оформить заказ'")
    def click_on_submit_order_button(self):
        submit_order_button = self.find_element_with_wait(MainPageLocators.SUBMIT_ORDER_BUTTON)
        self.click_on_element_js(submit_order_button)

    @allure.step("Проверка видимости окна заказа")
    def order_window_is_visible(self):
        order_window = self.find_element_with_wait(MainPageLocators.ORDER_WINDOW)
        return order_window.is_displayed()

    @allure.step("Закрытие окна заказа")
    def close_order_window(self):
        close_button = self.find_element_with_wait(MainPageLocators.CLOSE_ORDER_WINDOW_BUTTON)
        self.click_on_element_js(close_button)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        initial_value = '9999'
        self.wait_for_text_to_change(MainPageLocators.ORDER_NUMBER, initial_value)
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
