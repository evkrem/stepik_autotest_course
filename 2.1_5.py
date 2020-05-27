from selenium import webdriver
import time
import math
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)


  
 
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    l1 = browser.find_element_by_css_selector("[for=robotCheckbox]")
    l1.click()
    l2 = browser.find_element_by_css_selector("[for=robotsRule]")
    l2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()