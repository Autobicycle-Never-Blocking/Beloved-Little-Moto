def config():
    city_str = '北京、上海、广东、深圳、成都、杭州、重庆、武汉、西安、苏州、天津、南京、长沙、郑州、东莞、青岛、沈阳、宁波、昆明、无锡'
    city_list = city_str.split('、')

    position = {
        '产品线': ['产品经理', '数据产品经理'],
        '技术线': ['后端开发', '前端开发', '测试', '运维', 'Java', 'python', 'php'],
        '设计线': ['交互设计', 'UI设计', '原画师', '动画师'],
        '运营线': ['内容运营', '电商运营', '用户运营', '数据运营', '用户增长'],
        '算法线': ['AI', 'NLP', 'CV', 'BI', '算法工程师', '自然语言处理', '计算机视觉', '算法'],
    }
    return city_list, position

