from multiprocessing import Pool

from config import config
from core.lagou import LaGou, lagou_worker

if __name__ == '__main__':

    # city_list, _, _ = config()
    pool = Pool(processes=2)
    for i in range(2):
        pool.apply_async(lagou_worker('全国'))
    pool.close()
    pool.join()
