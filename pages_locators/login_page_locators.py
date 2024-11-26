from selenium.webdriver.common.by import By


class LoginPageLocators:

    RECOVER_PASSWORD_BTN = By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"
    LOGIN_EMAIL_INPUT = By.XPATH, "//input[@name='name']"
    LOGIN_PASSWORD_INPUT = By.XPATH, "//input[@name='Пароль']"
    LOGIN_SUBMIT_BUTTON = By.XPATH, "//Button[text()='Войти']"
