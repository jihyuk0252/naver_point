from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import pickle

options = webdriver.ChromeOptions() 
driver = webdriver.Chrome((ChromeDriverManager().install()), options=options)

def alert_process():
    first_tab = driver.window_handles[0]
    second_tab = driver.window_handles[1]
    driver.switch_to.window(window_name=first_tab )
    driver.close()
    driver.switch_to.window(window_name=second_tab)

def load_cookies():
    for cookie in pickle.load( open("./cookies.pkl", "rb") ):
        driver.add_cookie(cookie)

driver.get("http://naver.com")
time.sleep(1)
load_cookies()

driver.get("https://event2.pay.naver.com/event/benefit/list")
point_elements = driver.find_elements_by_xpath('//*[@id="eventList"]/li/a')
url_list = [element.get_attribute("href") for element in point_elements]

for url in url_list:
    driver.execute_script(f'window.open("{url}","_blank");''')
    time.sleep(2)
    alert_process()

time.sleep(1)
driver.get("https://event2.pay.naver.com/event/benefit/list")

driver.quit()