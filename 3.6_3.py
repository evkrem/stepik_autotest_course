from selenium import webdriver
import time
import math
import pytest

itog = ""
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(itog)

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])

def test_links(browser, link):    
    browser.get(link)
    browser.implicitly_wait(5)
    global itog
    answer = math.log(int(time.time()))
    print(answer)
    # button = browser.find_element_by_id("book")
    # button.click()


    input1 = browser.find_element_by_tag_name("textarea").send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission").click() 
    an = browser.find_element_by_css_selector(".smart-hints__hint")
    tx = an.text
    try:
        assert 'Correct!' == tx
    except AssertionError:
        itog += tx  # собираем ответ про Сов с каждой ошибкой


