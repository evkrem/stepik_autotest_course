from selenium import webdriver
import time
import math
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    print("x=: ", x)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    print("y=: ", y)
    
 
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)    
    l1 = browser.find_element_by_id("robotCheckbox")
    l1.click()
    l2 = browser.find_element_by_id("robotsRule")
    l2.click()

    # Отправляем заполненную форму
 #   button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    

    
