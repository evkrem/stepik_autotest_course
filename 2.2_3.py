from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element_by_id("num1")    
    x = x1.text
    print("x=: ", x)
    y1 = browser.find_element_by_id("num2")
    y = y1.text
    print("y=: ", y)

    z = str(int(x) + int(y))
    print("z=: ", z)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z).click()
    browser.find_element_by_css_selector("button.btn").click()
    #time.sleep(1)
    #button = browser.find_element_by_tag_name("button")
    button.click()

  
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()