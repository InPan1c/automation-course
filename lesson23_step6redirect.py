from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()

    #redirect
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Считаем
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)    

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    # Нажать на кнопку Submit
    submit = browser.find_element_by_tag_name('button')
    submit.click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()