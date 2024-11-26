from selenium.webdriver.common.by import By


class RecoverPasswordPageLocators:

    EMAIL_INPUT = By.XPATH, "//input[@name='name']"
    RECOVER_BUTTON = By.XPATH, "//button[contains(text(),'Восстановить')]"

