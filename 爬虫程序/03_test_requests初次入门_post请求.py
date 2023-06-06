import requests

url = "https://fanyi.baidu.com/sug"
data = {
    "kw":input("请输入一个单词：")
}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42"}

resp = requests.post(url,data=data)
print(resp.json())  #拿到的是json数据