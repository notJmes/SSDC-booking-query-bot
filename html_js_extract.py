import requests
import os
from selenium import webdriver
import time
from chromedriver_py import binary_path

# Prep
proj_path = os.path.dirname(os.path.realpath(__file__))+'/'

def get_html(url=''):
    # Prepare selenium to start
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(executable_path=binary_path)
    driver.minimize_window()
    driver.get(url)
    time.sleep(1)
    html = driver.execute_script('return document.getElementsByTagName("html")[0].innerHTML')
    driver.quit()
    return str(html)

if __name__ == '__main__':
    # html = str(get_html('https://www.ssdcl.com.sg/User/Login'))
    # with open('html.txt', 'wb') as f:
    #     f.write(html.encode())

    driver = webdriver.Chrome(proj_path+'chromedriver.exe')
    driver.get('https://www.ssdcl.com.sg/User/Login')
    time.sleep(1)
    html = driver.execute_script('return document.getElementsByTagName("html")[0].innerHTML')
    with open('html.txt', 'wb') as f:
        f.write(html.encode())
