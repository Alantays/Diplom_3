from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from urls import ORDER_FEED_PAGE, MAIN_PAGE
import allure


class TestMainFunctionality:

    @allure.title('Переход на страницу "Лента заказов"')
    @allure.description('При клике на кнопку "Лента заказов" происходит переход на страницу "Лента заказов"')
    def test_click_on_order_feed_button_successful(self, driver):
        main_page = MainPage(driver)
        current_url = main_page.click_on_order_feed_button(ORDER_FEED_PAGE)

        assert current_url == ORDER_FEED_PAGE

    @allure.title('Переход на страницу "Конструктор"')
    @allure.description('При клике на кнопку "Конструктор" происходит переход на страницу "Конструктор"')
    def test_click_on_constructor_button_successful(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_button(ORDER_FEED_PAGE)

        order_feed_page = OrderFeedPage(driver)
        current_url = order_feed_page.click_on_constructor_button(MAIN_PAGE)

        assert current_url == MAIN_PAGE

    @allure.title('Клик на ингредиент вызывает всплывающее окно с деталями')
    @allure.description('При клике на ингредиент отображается окно с информацией об ингредиенте')
    def test_click_on_ingredient_shows_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_details_is_visible = main_page.ingredient_details_window_is_visible()
        assert ingredient_details_is_visible is True

    @allure.title('Закрытие окна с деталями ингредиента')
    @allure.description('При клике на кнопку "Закрыть" окно с деталями ингредиента закрывается')
    def test_click_on_details_close_button_closes_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        is_modal_closed = main_page.close_ingredient_details_window()
        assert is_modal_closed is True

    @allure.title('Добавление ингредиента в корзину увеличивает счетчик ингредиента')
    @allure.description('При добавлении ингредиента в корзину, счетчик ингредиента увеличивается')
    def test_moving_ingredient_to_basket_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.move_ingredient_to_order()
        counter_increased = main_page.is_ingredient_counter_increased()

        assert counter_increased is True

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_create_order(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_and_get_credentials['email'])
        login_page.input_password(create_user_and_get_credentials['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_page_to_be_loaded()
        main_page.move_ingredient_to_order()
        main_page.click_on_submit_order_button()
        order_window_is_visible = main_page.order_window_is_visible()

        assert order_window_is_visible is True
