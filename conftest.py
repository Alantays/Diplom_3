import pytest
from selenium import webdriver
from urls import MAIN_PAGE, CREATE_USER_ENDPOINT, DELETE_USER_ENDPOINT
from helper import generate_user_data
import requests


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.set_window_size(1920, 1080)
    driver.get(MAIN_PAGE)

    yield driver
    driver.quit()


@pytest.fixture
def create_user_and_get_credentials():
    payload = generate_user_data()
    created_response = requests.post(CREATE_USER_ENDPOINT, json=payload)
    if created_response.status_code == 200:
        access_token = created_response.json()['accessToken']
        yield payload
        headers = {'Authorization': access_token}
        requests.delete(DELETE_USER_ENDPOINT, headers=headers)
    else:
        yield payload
