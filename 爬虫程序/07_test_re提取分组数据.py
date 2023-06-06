import re

# 想要提取数据必须用小括号括起来，可以单独起名字
# (?P<名字>正则)
# 提取数据的时候，需要group("名字")
s = """"
<div class='西游记'><span id='10010'>中国联通</span><div>
<div class='西游记'><span id='10086'>中国移动</span><div>
"""

obj = re.compile(r"<span id='(?P<number>\d+)'>(?P<name>.*?)</span>")
result = obj.finditer(s)
for item in result:
    number = item.group("number")
    print(number)
    name = item.group("name")
    print(name)