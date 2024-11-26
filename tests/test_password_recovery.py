from urls import FORGOT_PASS_PAGE, LOGIN_PAGE, RESET_PASS_PAGE
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from pages.recover_password_page import RecoverPasswordPage
import allure


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description(
        'При клике на кнопку "Восстановить пароль" происходит переход на страницу восстановления пароля.')
    def test_click_on_recover_password_button_successful(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button(LOGIN_PAGE)

        login_page = LoginPage(driver)
        current_url = login_page.click_on_recover_password_button()

        assert current_url == FORGOT_PASS_PAGE

    @allure.title('Ввод email и переход на страницу сброса пароля')
    @allure.description(
        'После ввода email на странице восстановления пароля, происходит переход на страницу для сброса пароля.')
    def test_input_email_and_click_on_recovery_password_button_successful(
            self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button(LOGIN_PAGE)

        login_page = LoginPage(driver)
        login_page.click_on_recover_password_button()

        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.input_email(create_user_and_get_credentials['email'])
        current_url = recover_password_page.click_on_recover_button(RESET_PASS_PAGE)

        assert current_url == RESET_PASS_PAGE

    @allure.title('Клик на иконку "Показать пароль" отображает пароль')
    @allure.description('При клике на иконку "глаз", пароль становится видимым на странице сброса пароля.')
    def test_clicking_on_eye_button_reveals_password(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button(LOGIN_PAGE)

        login_page = LoginPage(driver)
        login_page.click_on_recover_password_button()

        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.input_email(create_user_and_get_credentials['email'])
        recover_password_page.click_on_recover_button(RESET_PASS_PAGE)

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.click_on_eye_button()

        assert reset_password_page.is_password_visible()
