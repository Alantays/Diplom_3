import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from urls import PERSONAL_ACCOUNT_PAGE, MAIN_PAGE, ORDER_HISTORY_PAGE, LOGIN_PAGE


class TestPersonalAccount:
    @allure.title("Переход на страницу личного кабинета")
    @allure.description("Проверка перехода на страницу личного кабинета после входа в систему.")
    def test_click_on_personal_account_button_successful(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_and_get_credentials['email'])
        login_page.input_password(create_user_and_get_credentials['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_page_to_be_loaded()
        current_url = main_page.click_on_personal_account_button(PERSONAL_ACCOUNT_PAGE)

        assert current_url == PERSONAL_ACCOUNT_PAGE

    @allure.title("Переход на страницу 'История заказов'")
    @allure.description("Проверка перехода на страницу 'История заказов' по кнопке в личном кабинете.")
    def test_navigate_to_order_history_successful(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_and_get_credentials['email'])
        login_page.input_password(create_user_and_get_credentials['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_page_to_be_loaded()
        main_page.click_on_personal_account_button(PERSONAL_ACCOUNT_PAGE)

        personal_account_page = PersonalAccountPage(driver)
        current_url = personal_account_page.click_on_order_history_button(ORDER_HISTORY_PAGE)

        assert current_url == ORDER_HISTORY_PAGE

    @allure.title("Выход из аккаунта")
    @allure.description("Проверка выхода из аккаунта по кнопке 'Выход' в личном кабинете.")
    def test_logout_from_personal_account(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)
        login_page.input_login(create_user_and_get_credentials['email'])
        login_page.input_password(create_user_and_get_credentials['password'])
        login_page.click_on_login_submit_button()

        main_page.wait_page_to_be_loaded()
        main_page.click_on_personal_account_button(PERSONAL_ACCOUNT_PAGE)

        personal_account_page = PersonalAccountPage(driver)
        current_url = personal_account_page.logout(LOGIN_PAGE)

        assert current_url == LOGIN_PAGE
