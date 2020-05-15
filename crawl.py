import random
import time

from config import config
from core.lagou import LaGou

if __name__ == '__main__':

    city_list, position = config()
    for city in city_list:
        for type, keyword_list in position.items():
            for keyword in keyword_list:
                LaGou(keyword='java', city=city, type=type).spider()
                time.sleep(random.randint(1, 5))
