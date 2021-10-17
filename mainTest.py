from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import re
import random
import time
import requests
from lxml import html
from bs4 import BeautifulSoup as bs
import uuid

browser = webdriver.Chrome()
browser.maximize_window()  # 最大化視窗
wait = WebDriverWait(browser, 10)  # 等待載入10s

USEREMAIL = ''
PASSWORD = ''
LOGIN_URL = 'https://www.mobile01.com/login.php'


"""主程式"""
def main():
    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    my_uuid = uuid.uuid4()
    realUuid = str(my_uuid.hex)

    nowTime = int(time.time())  # 取得現在時間
    struct_time = time.localtime(nowTime)  # 轉換成時間元組
    time_stamp = str(int(time.mktime(struct_time)))  # 轉成時間戳
    print(time_stamp)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'MID-uuid=ead53f00-bc87-11eb-9bf9-83ee44459d28; MID-uuid-p=4015fb9560057012f3c99e92c09cf440; __retuid=9367b60e-c619-2d1f-7596-e536ca6713f; _ga=GA1.2.2135766407.1631189143; _gcl_au=1.1.1471991265.1631189143; _ss_pp_id=8ba5b9b3a69034cc1671621828950828; _td=ab682225-7645-4ac5-a3a0-edd07838b8df; PHPSESSID=' + realUuid + '; __fpid=4c7116cc061ba10e151b431634f2c694; _gid=GA1.2.1079404234.1634356408; __cfruid=e070a6a5a72f128da60a722f359ddb884b2b6d5b-1634365651; __retfs=fSes-9e592b64-2d4c-b900-6c3f; MID_id=2168609; HobbyCatuuid=6c5e19c9c4e308faa4b23beeeb898d9d; HobbyCat=1; vip_msg=1; theme=w;  __cf_bm=Us3.71pvSbcYx8_tsuWH82lR24IvcHEz221pdW7ZIxo-1634373621-0-AV1lQcTdI88iyEA+L0IcViig0a4rwZdJLBTi8wJ9DM6ZWA4DsF0fWx+W4jg5s0G/zmvAwfWYD8Z0NWKDsO6044CkEsXSCir8clcegaEBuEKBVxd2hj7im0yWumMS59Pz9d+QidGMc0eXGiVpgKCqPwzROxYVE6wMBPGZysVhX1uZbF8XWm50/uQPGXCpldWuEg==; userinfo[currentlogin]=' + time_stamp + '; userinfo[id]=2168609; userinfo[username]=%E7%99%BC%E5%91%86%E6%98%AF%E7%A8%AE%E4%BA%AB%E5%8F%97; userinfo[pass]=FdQWB7lF%2FKXwMV8G1KYl0%2Fl3TkT2C0oKg7IaCo4rdE8%3D; userinfo[lastlogin]=1420157160; loginstat=1; tagmode=1;',
        'referer': 'https://www.mobile01.com/login.php',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    payload = {
        'email': USEREMAIL,
        'password': PASSWORD
    }

    result = session_requests.post(LOGIN_URL, data=payload, headers=headers)
    print(result.text)
    # soup = bs(result.text, 'html.parser')
    # headers = {
    #     'Connection': 'keep-alive',
    #     'Content-Length': '103',
    #     'Cache-Control': 'max-age=0',
    #     'Origin': 'https://anewstip.com',
    #     'Upgrade-Insecure-Requests': '1',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Referer': LOGIN_URL,
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    #     'Cookie': '_ga=GA1.2.218269643.1513734952; _gid=GA1.2.1405785245.1513907212; csrftoken=' + authenticity_token + '; sessionid=yvb8vq6m4katwmz76d0cnjubd29pdrdb; _gat=1'
    # }
    # def login():
    #     browser.get('https://www.mobile01.com/login.php')
    #     input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="regEmail"]')))
    #     input.send_keys(USEREMAIL)
    #     t.sleep(3)
    #     input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="regPassword"]')))
    #     input.send_keys(PASSWORD)
    #     t.sleep(2)
    #     submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitBtn"]')))
    #     t.sleep(1)
    #     submit.click()  # 點選登入按鈕
    #     get_page_index()
    #
    # def get_page_index():
    #     browser.get('https://www.mobile01.com/topiclist.php?f=296.html')
    #     try:
    #         print(browser.page_source)  # 輸出網頁原始碼
    #     except Exception as e:
    #         print(str(e))
    #
    # login()

if __name__ == '__main__':
    main()
