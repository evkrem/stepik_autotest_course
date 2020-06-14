# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 12 секунд
    browser.implicitly_wait(12)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    ) # ждем, пока price станет равным 100
    button = browser.find_element_by_id("book")
    button.click()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print("x=: ", x)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    print("y=: ", y)
    # button = browser.find_element_by_tag_name("button")    
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)    
 
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button2 = browser.find_element_by_id("solve")
    button2.click()    
    

finally:
    time.sleep(5)
    browser.quit()