import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
import logging
import base
@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_convert_celsius_to_fahrenheit(browser):
    browser.get(base.URL)
    convert_from_field_temperature = browser.find_element_by_id(base.CONVERT_FROM_FIELD).send_keys(base.CELSIUS_TEXT)
    time.sleep(1)
    convert_to_field_temperature = browser.find_element_by_id(base.CONVERT_TO_FIELD).send_keys(base.FAHRENHEIT_TEXT)
    time.sleep(1)
    convert_values_field_temperature = browser.find_element_by_class_name(base.VALUES_FIELD).send_keys(base.INPUT_Values)
    time.sleep(1)
    convert_button_temperature = browser.find_element_by_xpath(base.CONVERT_BUTTON).click()
    time.sleep(1)
    find_converting_result_temperature = browser.find_element_by_id(base.ANSWER)
    get_converting_result_temperature = find_converting_result_temperature.text
    assert get_converting_result_temperature == '5°C= 41.00000°F'

def test_convert_meters_to_feet(browser):
    browser.get(base.URL)
    convert_from_field_distance = browser.find_element_by_id(base.CONVERT_FROM_FIELD).send_keys(base.METERS_TEXT)
    time.sleep(1)
    convert_to_field_distance = browser.find_element_by_id(base.CONVERT_TO_FIELD).send_keys(base.FEETS_TEXT)
    time.sleep(1)
    convert_values_field_distance = browser.find_element_by_class_name(base.VALUES_FIELD).send_keys(base.INPUT_Values)
    time.sleep(1)
    convert_button_distance = browser.find_element_by_xpath(base.CONVERT_BUTTON).click()
    time.sleep(1)
    find_converting_result_distance = browser.find_element_by_id(base.ANSWER)
    get_converting_result_distance = find_converting_result_distance.text
    assert get_converting_result_distance == '5m= 16ft 4.850394in'

def test_convert_ounces_to_grams(browser):
    browser.get(base.URL)
    convert_from_field_weight = browser.find_element_by_id(base.CONVERT_FROM_FIELD).send_keys(base.OUNCES_TEXT)
    time.sleep(1)
    convert_to_field_weight = browser.find_element_by_id(base.CONVERT_TO_FIELD).send_keys(base.GRAMS_TEXT)
    time.sleep(1)
    convert_values_field_WEIGHT = browser.find_element_by_class_name(base.VALUES_FIELD).send_keys(base.INPUT_Values)
    time.sleep(1)
    convert_button_WEIGHT = browser.find_element_by_xpath(base.CONVERT_BUTTON).click()
    time.sleep(1)
    find_converting_result_weight = browser.find_element_by_id(base.ANSWER)
    get_converting_result_weight = find_converting_result_weight.text
    assert get_converting_result_weight == '5oz= 141.7476g'




