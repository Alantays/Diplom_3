from selenium.webdriver.common.by import By


class MainPageLocators:

    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
    MAIN_PAGE_HEADER = By.XPATH, "//h1[contains(text(),'Соберите бургер')]"
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"
    ORDER_FEED_BUTTON = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    INGREDIENT = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"
    INGREDIENT_DETAILS_WINDOW = By.XPATH, "//h2[contains(text(),'Детали ингредиента')]"
    CLOSE_DETAILS_WINDOW_BUTTON = By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button"
    MODAL_ELEMENT = By.CSS_SELECTOR, "section.Modal_modal__P3_V5"
    BASKET = By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']"
    INGREDIENT_COUNTER = By.XPATH, "//p[@class='counter_counter__num__3nue1']"
    SUBMIT_ORDER_BUTTON = By.XPATH, "//button[contains(text(),'Оформить заказ')]"
    ORDER_WINDOW = By.XPATH, "//p[text()='идентификатор заказа']"
    CLOSE_ORDER_WINDOW_BUTTON = By.XPATH, "//button[@type='button']"
    ORDER_NUMBER = By.XPATH, "//h2[contains(@class,'Modal_modal__title')]"
