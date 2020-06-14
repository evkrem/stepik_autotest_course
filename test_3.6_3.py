import pytest
from selenium import webdriver
import time
import math


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
# вызываем фикстуру в тесте, передав ее как параметр
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    answer = math.log(int(time.time()))
    print('answer')
