from sqlalchemy import text

from utils.db import local_db


def insert(tablename, **kwargs):
    columns = ','.join([k for k in kwargs.keys()])  # 列名称
    values = ','.join(['"' + str(v) + '"' for v in kwargs.values()])
    # print(values)
    # 拼接sql字符串
    sql = 'insert into ' + tablename + ' (' + columns + ') values (' + values + ');'
    print(sql)
    db = local_db()
    try:
        result = db.engine.execute(text(sql))
        result.close()
        print('insert success!')
        return 1
    except Exception as e:
        return 0


if __name__ == '__main__':
    dict_res = {'positionName': 'java工程师', 'district': '朝阳区', 'stationname': '望京东', 'jobNature': '全职',
                'companyLabelList': ['年底双薪', '绩效奖金', '股票期权', '带薪年假'], 'industryField': '数据服务,移动互联网',
                'salary': '15k-25k', 'companySize': '15-50人', 'skillLables': ['Java', '服务器端'],
                'createTime': '2020-05-15 17:08:43', 'companyFullName': '北京麒麟心通网络技术有限公司', 'workYear': '3-5年',
                'education': '本科', 'positionAdvantage': '福利好，大牛多，氛围好', 'url': 'https://www.lagou.com/jobs/5816866.html',
                'detail': '岗位要求：1、本科及以上学历,有扎实的计算机基本功和coding能力2、熟练掌握java及面向对象设计开发,对部分开源框架有深入研究3、了解SOA的架构理念,熟悉常用的设计模式4、熟练掌握Mysql应用开发,数据库原理及其性能优化的常用技术,熟悉Redis,ES等开源系统5、熟悉socket编程,深入理解tcp/ip传输协议6、精通多线程/多进程的开发,精通并发,网络,io等基础知识,熟悉JVM7、熟练linux,shell,python脚本编写,熟悉相关编程开发8、拥有和工作年限相称的广度或深度,有较强的逻辑思维能力,善于分析,归纳,描述,沟通和解决问题9、做事严谨认真,要有强烈的责任感,善于学习,热爱技术10、拥有良好的自我驱动能力'}

    insert('jobs', **dict_res)
