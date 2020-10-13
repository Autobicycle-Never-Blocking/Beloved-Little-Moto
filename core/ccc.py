from selenium import webdriver
import time


def get_video_src(url):
    driver = webdriver.Chrome('./chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(6)
    # driver.get("https://www.imdb.com/video/vi1874967321?playlistId=tt0111161&ref_=vp_rv_ap_0")
    driver.get(url)
    time.sleep(1)

    element = driver.find_elements_by_xpath('//*[@class="video-player__video"]//video')
    element1 = driver.find_elements_by_xpath('//*[@class="ipc-page-grid__item ipc-page-grid__item--span-1"]//h3')
    src = element[0].get_attribute("src")
    title = element1[0].text
    detail = element1[1].text
    driver.quit()
    return src, title, detail


if __name__ == '__main__':
    print(get_video_src('https://www.imdb.com/video/vi1874967321?playlistId=tt0111161&ref_=vp_rv_ap_0'))
