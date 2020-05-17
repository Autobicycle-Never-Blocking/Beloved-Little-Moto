import threading

import requests
from lxml import etree

from config import config
from utils.common import get_header
from utils.db_utils import insert
from collections import Counter


class LaGou(object):

    def __init__(self, thread=12):
        # self.keyword = keyword
        self.thread = thread
        # self.city = city
        # self.type = type
        self.baseurl = 'https://www.lagou.com/jobs/positionAjax.json'
        self.header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }

    def spider(self, keyword, city, type):

        expanded_skills = []

        max_page = 10
        for i in range(1, max_page):
            s = requests.Session()
            s.get(
                url='https://www.lagou.com/jobs/list_运维?city=北京&cl=false&fromSearch=true&labelWords=&suginput=',
                headers=get_header(), timeout=3)
            cookie = s.cookies
            res = requests.post(self.baseurl, headers=self.header, data={'first': True, 'pn': i, 'kd': keyword},
                                params={'px': 'default', 'city': city, 'needAddtionalResult': 'false'},
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
                # print(detail)

                related_skills = data.get('skillLables')

                data_dict = {
                    "firstType": str(data.get('firstType')),
                    "secondType": str(data.get('secondType')),
                    "thirdType": str(data.get('thirdType')),
                    "city": str(data.get("city")),
                    "positionName": str(data.get('positionName')),
                    "district": str(data.get('district')),
                    "stationname": str(data.get('stationname')),
                    "jobNature": str(data.get('jobNature')),
                    "companyLabelList": str(data.get('companyLabelList')),
                    "industryField": str(data.get('industryField')),
                    "salary": str(data.get('salary')),
                    "companySize": str(data.get('companySize')),
                    "skillLables": str(related_skills),
                    "createTime": str(data.get('createTime')),
                    "companyFullName": str(data.get('companyFullName')),
                    "workYear": str(data.get('workYear')),
                    "education": str(data.get('education')),
                    "positionAdvantage": str(data.get('positionAdvantage')),
                    "url": str(url),
                    "detail": str(detail),
                    "type": str(type),
                    "latitude": str(data.get("latitude")),
                    "longitude": str(data.get("longitude")),
                    "keyword": str(keyword),
                }
                # print(data_dict)
                # time.sleep(random.randint(1, 5))

                expanded_skills += related_skills

                # print(related_skills)

                if not insert('lagou_copy1_copy1', **data_dict):
                    continue

        return [s.lower() for s in expanded_skills]

    def run(self):
        _, position, init_job = config()
        visited_jobs = set()
        thread_list = []
        for i in range(self.thread):
            t = threading.Thread(target=self.lagou_worker, args=(init_job, position, visited_jobs))
            thread_list.append(t)
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        for t in thread_list:
            t.join()

    def lagou_worker(self, init_job, position, visited_jobs):

        while init_job:
            search_job = init_job.pop(0)

            print('We need to search {}, now search {}'.format(init_job, search_job))

            if search_job in visited_jobs:
                continue
            type = ''
            for k, v in position.items():
                if search_job in v:
                    type = k

            new_expaned = self.spider(search_job, '无锡', type)

            expaned_counter = Counter(new_expaned).most_common(n=5)

            new_jobs = [j for j, n in expaned_counter]

            init_job += new_jobs

            visited_jobs.add(search_job)


if __name__ == '__main__':

    LaGou().run()
