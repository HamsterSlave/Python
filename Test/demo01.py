import requests
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
}
res = requests.get('http://bj.xiaozhu.com/search-duanzufang-p2-0/',headers=headers)
try:
    print(str(res) + " 访问成功！")
    print(res.text)
except ConnectionError:
    print("拒绝访问！")