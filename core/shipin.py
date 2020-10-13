import requests
from collections import Counter

from lxml import etree

from utils.common import get_header


class ShiPin(object):

    def __init__(self, thread=12):
        self.baseurl = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
        self.header = {
            # 'cookie': 'uu=BCYpvRkImjqxo5FSnOh8xO5AR2q1MmrGgmTDsOkkCiHyQsR4NYhUATi211BLZud04XRl8Uh0j0fJ%0D%0Al3NUjXqKxZPmuVnavB8MektyniygyNydLk87tqXfNfha0i-zo1wlTt12zaAGj7UnelojDkLw0f3S%0D%0Amw%0D%0A; session-id=139-9802704-1913818; adblk=adblk_no; ubid-main=130-6052127-9559554; session-id-time=2082787201l; session-token=0eAWRbW7vqw800cBqoyOsKjVcmOTRpnPAbITqGXxDTmlLUiCArpjtdQO6XNxY9aNCQ7S+lFA8zTcPQ90AfTNrS1KfzhDWPmXOdu+yUmCYK1tKjzMf9UuAENhGDNCe2vBbGvXv0UIFIPuNR5Gc8Mnsv8Qx/2tikKGFRuSU00Nq4hdut8thuyqMvya7O/qpujz; as=%7B%22n%22%3A%7B%7D%7D; csm-hit=tb:8EZFTJHN1S1K2SQZ8D49+s-9DRXW5YT1NH7JC8A5Z9S|1602496425192&t:1602496425192&adb:adblk_no',
            'referer': 'https://www.imdb.com/title/tt0758758/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=K7SXKN76FTKF60X6Y2RQ&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_214',
            'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }

    def spider(self):
        data = []
        s = requests.Session()
        s.get(url=self.baseurl, headers=get_header(), timeout=5)
        cookie = s.cookies
        res = requests.get(self.baseurl, headers=self.header, cookies=cookie, timeout=5)
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        url_str = 'https://www.imdb.com'
        # img_src = ''.join(
        #     html.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td/a/img/@src')).strip()
        # detail_url = ''.join(html.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[1]/a/@href')).strip()

        detail_url_list = html.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[1]/a/@href')
        # img_src_list = html.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td/a/img/@src')
        for j in [url_str + i for i in detail_url_list]:
            print(j)
            s1 = requests.Session()
            s1.get(url=j, headers=get_header(), timeout=5)
            cookie1 = s1.cookies
            # self.header['referer'] = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
            response = requests.get(j, headers=self.header, cookies=cookie1, timeout=5)
            response.encoding = 'utf-8'
            de_html = etree.HTML(response.text)
            # print(res.text)
            title = de_html.xpath('//*[@id="title-overview-widget"]//h1/text()')[0]
            img_src = de_html.xpath('//*[@class="slate"]//img/@src')[0]
            video_url = url_str + de_html.xpath('//*[@class="slate"]/a/@href')[0]
            # print(img_src)
            # print(title)
            print(video_url)
            s2 = requests.Session()
            s2.get(url=video_url, headers=get_header(), timeout=5)
            cookie2 = s2.cookies
            res_video = requests.get(video_url, headers=self.header, cookies=cookie2, timeout=5)
            res_video.encoding = 'utf-8'
            video_html = etree.HTML(res_video.text)
            print(res_video.text)
            video_src = video_html.xpath('//*[@id="imdb-jw-video-1"]//@src')
            print(video_src)
            video_detail = video_html.xpath('//*[@class="ipc-page-grid__item ipc-page-grid__item--span-1"]//h3/text()')
            print(video_src)
            video_dict = {
                'title': title,
                'img_src': img_src,
                'video_src': video_src,
                'video_detail': video_detail,
            }
            data.append(video_dict)
        print(data)
        with open('video.txt', 'w') as f:
            f.write(str(data))

    def run(self):
        self.spider()


if __name__ == '__main__':
    ShiPin().run()
