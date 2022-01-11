import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pyperclip
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

driver = webdriver.Chrome('C:/Users/327ae/Downloads/chromedriver_win32/chromedriver.exe')

uid = '000'
upw = '000'

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
driver.implicitly_wait(10)
tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('pw')

tag_id.click()
pyperclip.copy(uid) 
tag_id.send_keys(Keys.CONTROL, 'v') 
time.sleep(1)

tag_pw.click() 
pyperclip.copy(upw) 
tag_pw.send_keys(Keys.CONTROL, 'v') 
time.sleep(1)

login_btn = driver.find_element_by_id('log.login') 
login_btn.click() 
time.sleep(2)

driver.get('https://mail.naver.com/')
html = driver.page_source

soup = BeautifulSoup(html, 'lxml')
title_list =  soup.find_all('strong', 'mail_title')
sending_list = soup.find_all('div','name _ccr(lst.from)')
sending=[]
title=[]
for titles in title_list:
    print(titles.text)
    title.append(titles.text)
    
for sendings in sending_list:
    print(sendings.text)
    sending.append(sendings.text)
    
data_fr = pd.DataFrame({
    '발신자' : sending,
    '메일 제목' : title
    }
)
data_fr.to_excel('mail_title.xlsx')


# for titles in my_titles:
#     print(titles.text)
    
# with requests.Session() as S:

#     login_req = S.post('http://www.ssodam.com/', data=LOGIN_INFO)

#     print(login_req.status_code)

#     soup = BeautifulSoup(html,'html.parser')

#     my_titles = soup.select(
#         'h3 > a'
#     )

