import requests
import hashlib


def get_video(url):
    header = {
        # 'cookie': 'uu=BCYpvRkImjqxo5FSnOh8xO5AR2q1MmrGgmTDsOkkCiHyQsR4NYhUATi211BLZud04XRl8Uh0j0fJ%0D%0Al3NUjXqKxZPmuVnavB8MektyniygyNydLk87tqXfNfha0i-zo1wlTt12zaAGj7UnelojDkLw0f3S%0D%0Amw%0D%0A; session-id=139-9802704-1913818; adblk=adblk_no; ubid-main=130-6052127-9559554; session-id-time=2082787201l; session-token=0eAWRbW7vqw800cBqoyOsKjVcmOTRpnPAbITqGXxDTmlLUiCArpjtdQO6XNxY9aNCQ7S+lFA8zTcPQ90AfTNrS1KfzhDWPmXOdu+yUmCYK1tKjzMf9UuAENhGDNCe2vBbGvXv0UIFIPuNR5Gc8Mnsv8Qx/2tikKGFRuSU00Nq4hdut8thuyqMvya7O/qpujz; as=%7B%22n%22%3A%7B%7D%7D; csm-hit=tb:8EZFTJHN1S1K2SQZ8D49+s-9DRXW5YT1NH7JC8A5Z9S|1602496425192&t:1602496425192&adb:adblk_no',
        'referer': 'https://www.imdb.com/title/tt0758758/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=K7SXKN76FTKF60X6Y2RQ&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_214',
        'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    # url = 'https://imdb-video.media-imdb.com/vi1874967321/1434659607842-pgv4ql-1531864355086.mp4?Expires=1602588206&Signature=LywaT-QUThXAliaxB3w05rPIoWCRAE4RVx575MQJVoIxjzWDqiokaDQ7BJF117HR4QYRKUTD3krOrshkaQ6qkABIEJwZOGPJwAr9h4x7TBM~b2-Fgh91p2zn0VbvGGWys2aNABOBqIy8uFsOcZRu1qxgVcRbnj4N1J6QdjRTZR4t5C6OSVwgEhGoOwSLfZA3SXyanOZrPm~Uoum8WAC8oJ07tB4zNxcUjcFnc-aNrA-1Cdul-uq5w~1rPIrmIMTwFcd3wxT5syvkeLmh8eskvik0Yf9yEagCR32WnBD4GTi5rkpaPoHJI46zD-7NMrEx0opNrEXFnjeuo5RJhJUnUA__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA'
    res = requests.get(url, headers=header)
    aaa = res.content

    md5_1 = hashlib.md5()
    md5_1.update(aaa)
    # while 1:
    #     data = f.read(Bytes=1024)  # 由于是一个文件，每次只读取固定字节
    #     if data:  # 当读取内容不为空时对读取内容进行update
    #         md5_1.update(data)
    #     else:  # 当整个文件读完之后停止update
    #         break
    ret = md5_1.hexdigest()

    with open(f'video/{ret}.mp4', 'wb') as f:
        f.write(aaa)
