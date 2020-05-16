from multiprocessing import Pool

from config import config
from core.lagou import LaGou, lagou_worker

if __name__ == '__main__':
    # city_list, _, _ = config()
    # pool = Pool(processes=len(city_list))
    # for i in [lagou_worker(j) for j in city_list]:
    #     pool.apply_async(i)
    # pool.close()
    # pool.join()
    lagou_worker('全国')
