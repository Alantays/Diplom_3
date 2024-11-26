from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from urls import ORDER_FEED_PAGE, MAIN_PAGE, ORDER_HISTORY_PAGE, PERSONAL_ACCOUNT_PAGE
import allure


class TestOrderFeedSection:

    @allure.title('Клик на заказ отображает окно с деталями заказа')
    @allure.description('При клике на заказ из "Ленты заказов", появляется окно с деталями заказа.')
    def test_click_on_order_shows_order_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_button(ORDER_FEED_PAGE)

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_order()
        order_details_window_is_visible = order_feed_page.order_details_window_is_visible()

        assert order_details_window_is_visible

    @allure.title('Заказ из истории пользователя отображается в ленте заказов')
    @allure.description('После оформления заказа он появляется в ленте заказов пользователя.')
    def test_order_from_users_history_is_in_order_feed(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_and_get_credentials['email'])
        login_page.input_password(create_user_and_get_credentials['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_page_to_be_loaded()
        main_page.move_ingredient_to_order()
        main_page.click_on_submit_order_button()
        main_page.close_order_window()
        main_page.click_on_personal_account_button(PERSONAL_ACCOUNT_PAGE)

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_on_order_history_button(ORDER_HISTORY_PAGE)
        created_order_number = personal_account_page.get_order_number_from_orders_history()
        personal_account_page.click_on_order_feed_button(ORDER_FEED_PAGE)

        order_feed_page = OrderFeedPage(driver)
        order_number_is_in_list = order_feed_page.is_order_number_in_list(created_order_number)

        assert order_number_is_in_list

    @allure.title('Создание заказа увеличивает общий счетчик заказов')
    @allure.description('После создания нового заказа общий счетчик заказов в ленте заказов увеличивается.')
    def test_creating_order_increases_all_time_counter(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_and_get_credentials['email'])
        login_page.input_password(create_user_and_get_credentials['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_page_to_be_loaded()
        main_page.click_on_order_feed_button(ORDER_FEED_PAGE)

        order_feed_page = OrderFeedPage(driver)
        initial_orders_amount = order_feed_page.get_all_time_counter_number()
        order_feed_page.click_on_constructor_button(MAIN_PAGE)

        main_page.move_ingredient_to_order()
        main_page.click_on_submit_order_button()
        main_page.close_order_window()
        main_page.click_on_order_feed_button(ORDER_FEED_PAGE)
        all_time_counter_increased = order_feed_page.is_all_time_counter_increased(initial_orders_amount)
        assert all_time_counter_increased

    @allure.title('Создание заказа увеличивает счетчик заказов за сегодня')
    @allure.description('После создания нового заказа счетчик заказов за сегодня в ленте заказов увеличивается.')
    def test_creating_order_increases_day_counter(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_and_get_credentials['email'])
        login_page.input_password(create_user_and_get_credentials['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_page_to_be_loaded()
        main_page.click_on_order_feed_button(ORDER_FEED_PAGE)

        order_feed_page = OrderFeedPage(driver)
        initial_orders_amount = order_feed_page.get_today_counter_number()
        order_feed_page.click_on_constructor_button(MAIN_PAGE)

        main_page.move_ingredient_to_order()
        main_page.click_on_submit_order_button()
        main_page.close_order_window()
        main_page.click_on_order_feed_button(ORDER_FEED_PAGE)
        today_counter_increased = order_feed_page.is_today_counter_increased(initial_orders_amount)
        assert today_counter_increased

    @allure.title('Созданный заказ отображается в разделе "В работе"')
    @allure.description('После создания заказа, он отображается в разделе "В работе" ленты заказов.')
    def test_created_order_is_in_in_work_section(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_and_get_credentials['email'])
        login_page.input_password(create_user_and_get_credentials['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_page_to_be_loaded()
        main_page.move_ingredient_to_order()
        main_page.click_on_submit_order_button()
        created_order_number = main_page.get_order_number()
        main_page.close_order_window()
        main_page.click_on_order_feed_button(ORDER_FEED_PAGE)

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_order_to_appear(created_order_number)
        order_in_work = order_feed_page.is_order_number_in_work_list(created_order_number)

        assert order_in_work
