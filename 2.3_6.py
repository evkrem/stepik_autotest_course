from selenium import webdriver
import time
import math
import os
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    first_window = browser.window_handles[0]
    
    # button = browser.find_element_by_tag_name("button").click()


    x = browser.find_element_by_id("input_value")
    x_el = int(x.text)
    print(x_el)
    y = str(math.log(abs(12*math.sin(x_el))))
    browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_tag_name("button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    
    browser.switch_to.window(first_window)
    
    # input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    # input1.send_keys("John")
    # input2 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    # input2.send_keys("Smith")
    # input3 = browser.find_element_by_css_selector("[placeholder='Enter email']")
    # input3.send_keys("zzz@ukr.net")
   
    # current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    # print(current_dir)
    # file_path = os.path.join(current_dir, '111.txt')           # добавляем к этому пути имя файла 
    # print(file_path)
    # addf = browser.find_element_by_css_selector("[type='file']")
# #    addf.click()    
    # addf.send_keys(file_path)

    # # Отправляем заполненную форму

    # alert = browser.switch_to.alert
    # alert.accept()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    

    

