from multiprocessing import Pool

from config import config
from core.boss import Boss
from core.lagou import LaGou
from core.qcwy import QCWY

if __name__ == '__main__':
    # city_list, _, _ = config()
    # pool = Pool(processes=len(city_list))
    # for i in [lagou_worker(j) for j in city_list]:
    #     pool.apply_async(i)
    # pool.close()
    # pool.join()
    LaGou().run()
    # city_list, _, keyword_list = config()
    # pool = Pool(processes=2)
    # for city in city_list:
    #     for keyword in keyword_list:
    #         for i in [QCWY(city=city, keyword=keyword).run(),
    #                   Boss(city=city, keyword=keyword).Spider()]:
    #             pool.apply_async(i)
    # pool.close()
    # pool.join()
