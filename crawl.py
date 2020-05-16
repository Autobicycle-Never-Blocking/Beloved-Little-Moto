from multiprocessing import Pool

from config import config
from core.lagou import LaGou, lagou_worker

if __name__ == '__main__':

    city_list, _, _ = config()
    pool = Pool(processes=len(city_list))
    for i in [lagou_worker(j) for j in city_list]:
        pool.apply_async(i)
    pool.close()
    pool.join()
    # for city in city_list:
    #     for type, keyword_list in position.items():
    #         for keyword in keyword_list:
    #             LaGou(keyword=keyword, city=city, type=type).spider()
    #             time.sleep(random.randint(1, 5))
