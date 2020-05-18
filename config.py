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
    s_type = []
    for i in position.values():
        s_type.extend(i)

    return city_list, position, s_type


def color_list():
    colorList = [[
        '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
        '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
        '#1e90ff', '#ff6347', '#7b68ee', '#d0648a', '#ffd700',
        '#6b8e23', '#4ea397', '#3cb371', '#b8860b', '#7bd9a5'
    ],
        [
            '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
            '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
            '#1e90ff', '#ff6347', '#7b68ee', '#00fa9a', '#ffd700',
            '#6b8e23', '#ff00ff', '#3cb371', '#b8860b', '#30e0e0'
        ],
        [
            '#929fff', '#9de0ff', '#ffa897', '#af87fe', '#7dc3fe',
            '#bb60b2', '#433e7c', '#f47a75', '#009db2', '#024b51',
            '#0780cf', '#765005', '#e75840', '#26ccd8', '#3685fe',
            '#9977ef', '#f5616f', '#f7b13f', '#f9e264', '#50c48f'
        ]][0]
    return colorList
