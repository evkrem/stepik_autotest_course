from selenium import webdriver
import time
import math
import os
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
  
 
    input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    input1.send_keys("John")
    input2 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    input2.send_keys("Smith")
    input3 = browser.find_element_by_css_selector("[placeholder='Enter email']")
    input3.send_keys("zzz@ukr.net")
   
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    print(current_dir)
    file_path = os.path.join(current_dir, '111.txt')           # добавляем к этому пути имя файла 
    print(file_path)
    addf = browser.find_element_by_css_selector("[type='file']")
#    addf.click()    
    addf.send_keys(file_path)

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
    
    

    

