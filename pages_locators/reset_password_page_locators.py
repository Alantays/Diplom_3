from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    EYE_BUTTON = By.XPATH, "//div[@class='input__icon input__icon-action']"
    RESET_PASSWORD_INPUT = By.XPATH, "//input[@name='Введите новый пароль']"
