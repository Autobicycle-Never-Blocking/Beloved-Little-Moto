import random

from config import color_list


def get_position_list(df, num):
    colorList = color_list()
    company_list = list(set(df['companyFullName']))
    positionList = []
    for i in range(num):
        color_index = random.randint(0, 19)
        company_index = random.randint(0, len(company_list)-1)
        positionList.append(
            {
                "name": company_list[company_index],
                "value": random.randint(1000, 1500),
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
        company_list.remove(company_list[company_index])

    return positionList
