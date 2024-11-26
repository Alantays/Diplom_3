#URLs

MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'

REGISTER_PAGE = MAIN_PAGE + 'register'
LOGIN_PAGE = MAIN_PAGE + 'login'
FORGOT_PASS_PAGE = MAIN_PAGE + 'forgot-password'
RESET_PASS_PAGE = MAIN_PAGE + 'reset-password'
PERSONAL_ACCOUNT_PAGE = MAIN_PAGE + 'account/profile'
ORDER_HISTORY_PAGE = MAIN_PAGE + 'account/order-history'
ORDER_FEED_PAGE = MAIN_PAGE + 'feed'

#ENDPOINTS

BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
CREATE_USER_ENDPOINT = BASE_URL + 'auth/register'
DELETE_USER_ENDPOINT = BASE_URL + 'auth/user'
