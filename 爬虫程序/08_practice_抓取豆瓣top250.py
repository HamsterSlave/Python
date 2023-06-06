# 1、拿到页面源代码
# 2、编写正则，提取页面数据
# 3、保存数据
import re
import requests

f = open("top250.csv",mode="w",encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42"
}
for i in range(10):
    start = i * 25
    url = "https://movie.douban.com/top250?start={}&filter=".format(start)
    resp = requests.get(url, headers=headers)
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p class="">.*?导演: (?P<dao>.*?)&nbsp;.*?<br>'
                     r'(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
                     r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)
    result = obj.finditer(resp.text)

    for item in result:
        name = item.group("name")
        dao = item.group("dao")
        year = item.group("year").strip()
        score = item.group("score")
        num = item.group("num")
        f.write(f"{name},{dao},{year},{score},{num}\n")

f.close()
resp.close()
print("豆瓣top250提取完毕")
