import random
import time

import requests
from lxml import etree

from utils.common import get_header
from utils.db_utils import insert


class LaGou(object):

    def __init__(self, keyword, city, type):
        self.keyword = keyword
        self.city = city
        self.type = type
        self.baseurl = 'https://www.lagou.com/jobs/positionAjax.json'
        self.header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }

    def spider(self):
        for i in range(1, 31):
            s = requests.Session()
            s.get(
                url='https://www.lagou.com/jobs/list_运维?city=北京&cl=false&fromSearch=true&labelWords=&suginput=',
                headers=get_header(), timeout=3)
            cookie = s.cookies
            res = requests.post(self.baseurl, headers=self.header, data={'first': True, 'pn': i, 'kd': self.keyword},
                                params={'px': 'default', 'city': self.city, 'needAddtionalResult': 'false'},
                                cookies=cookie, timeout=3)
            text = res.json()
            all_data = text['content']['positionResult']['result']
            for data in all_data:
                s = requests.Session()
                s.get(
                    url='https://www.lagou.com/jobs/list_运维?city=北京&cl=false&fromSearch=true&labelWords=&suginput=',
                    headers=get_header(), timeout=3)
                cookie1 = s.cookies
                url = 'https://www.lagou.com/jobs/' + str(data.get('positionId')) + '.html'
                req1 = requests.get(url, headers=self.header, cookies=cookie1)
                req1.encoding = 'utf-8'
                html = etree.HTML(req1.text)
                detail = ''.join(html.xpath('//*[@class="job-detail"]//*/text()')).strip()
                if detail.isspace():
                    detail = ''.join(html.xpath('//*[@class="job-detail"]/text()')).strip()
                print(detail)
                data_dict = {
                    "positionName": str(data.get('positionName')),
                    "district": str(data.get('district')),
                    "stationname": str(data.get('stationname')),
                    "jobNature": str(data.get('jobNature')),
                    "companyLabelList": str(data.get('companyLabelList')),
                    "industryField": str(data.get('industryField')),
                    "salary": str(data.get('salary')),
                    "companySize": str(data.get('companySize')),
                    "skillLables": str(data.get('skillLables')),
                    "createTime": str(data.get('createTime')),
                    "companyFullName": str(data.get('companyFullName')),
                    "workYear": str(data.get('workYear')),
                    "education": str(data.get('education')),
                    "positionAdvantage": str(data.get('positionAdvantage')),
                    "url": str(url),
                    "detail": str(detail),
                    "type": str(self.type),
                }
                print(data_dict)
                time.sleep(random.randint(1, 5))
                if not insert('jobs', **data_dict):
                    continue


if __name__ == '__main__':
    LaGou(keyword='java', city='北京', type='产品线').spider()
