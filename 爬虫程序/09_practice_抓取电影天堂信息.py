"""
1、提取到主页面中每个电影背后的url地址
    -拿到“2023必看热片”那一块的代码
    -从拿到的代码中提取href的值
2、访问子页面，提取到电影名称及下载地址
"""
import requests
import re

url = "https://www.dy2018.com/"
resp = requests.get(url)
resp.encoding = "gbk"
# print(resp.text)

obj1 = re.compile(r"2023必看热片.*?<ul>(?P<html>.*?)</ul>",re.S)
result1 = obj1.search(resp.text)
html = result1.group("html").strip()
# print(html)

obj2 = re.compile(r"<li><a href='(?P<url1>.*?)'" ,re.S)
result2 = obj2.finditer(html)
obj3 = re.compile(r'<div id="Zoom">.*?◎片　　名　(?P<name>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<address>.*?)">', re.S)
for item in result2:
    url1 = item.group("url1")
    url2 = url.strip("/") + url1
    # print(url2)
    resp1 = requests.get(url2)
    resp1.encoding = "gbk"
    # print(resp1.text)
    result3 = obj3.finditer(resp1.text)
    for i in result3:
        name = i.group("name")
        address = i.group("address")
        print(name + "\n" + address + "\n")





