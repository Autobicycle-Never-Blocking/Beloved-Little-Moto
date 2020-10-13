import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Imdb():
    def __init__(self, username, password):
        os.system('pkill -f phantom')
        self.url = 'https://www.imdb.com/video/vi1874967321?playlistId=tt0111161&ref_=vp_rv_ap_0'
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1050, 840)
        self.wait = WebDriverWait(self.browser, 20)

    def open(self):
        """
        打开网页输入用户名密码并点击
        :return: None
        """
        self.browser.get(self.url)

    def run(self):
        """
        破解入口
        :return:
        """
        self.open()
        WebDriverWait(self.browser, 30).until(
            EC.title_is('我的首页')
        )
        cookies = self.browser.get_cookies()
        cookie = [item["name"] + "=" + item["value"] for item in cookies]
        cookie_str = '; '.join(item for item in cookie)
        self.browser.quit()
        return cookie_str