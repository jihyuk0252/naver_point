import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() 
options.add_argument('log-level=3')
options.add_argument('--mute-audio')
options.add_argument('--window-size=1920,1080')
options.add_argument("--disable-extensions")
options.add_argument('--start-maximized')
options.add_argument("./")

driver = webdriver.Chrome((ChromeDriverManager().install()), options=options)

def save_cookies():
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

driver.get("https://naver.com")
input("로그인 후 터미널에서 엔터를 눌러주세요.")
save_cookies()