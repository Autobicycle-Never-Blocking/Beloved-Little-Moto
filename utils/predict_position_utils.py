import random

from config import color_list


def get_position_list(df, num):
    colorList = color_list()
    company_list = df['companyFullName']
    positionList = []
    for i in range(num):
        color_index = random.randint(0, 19)
        positionList.append(
            {
                "name": company_list[random.randint(5, 10000)],
                "value": random.randint(1000,1500),
                "symbolSize": random.randint(40,80),
                "draggable": 'true',
                "itemStyle": {
                    "normal": {
                        "shadowBlur": 100,
                        "shadowColor": colorList[color_index],
                        "color": colorList[color_index]
                    }
                }
            }
        )

    return positionList
