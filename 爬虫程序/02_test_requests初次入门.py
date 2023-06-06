import requests

content = input("请输入你要检索的内容：")
URL = f"http://www.sogou.com/web?query={content}"
headers  =  {"User-Agent":"Mozilla/5.0  (Windows  NT  6.1;  Win64;  x64)  AppleWebKit/537.36  (KHTML,  like  Gecko)  Chrome/108.0.0.0  Safari/537.36  Edg/108.0.1462.42"}

resp = requests.get(URL,headers=headers)
resp.encoding = "utf-8"
print(resp.text)