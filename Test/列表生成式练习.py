import os
# 列表生成式，for循环后面还可以加上if判断
r = [x*x for x in range(1,11) if x % 2 == 0]
print(r)
# 两层循环
r1 = [m+n for m in '123' for n in 'ABC']
print(r1)
# 列出当前目录下的所有文件和目录名
r2 = [d for d in os.listdir('.')]
print(r2)
# 字典
d = {'1':'A','2':'B','3':'C'}
r3 = [k + '=' + v for k,v in d.items()]
print(r3)
# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
r4 = [s.lower() for s in L]
print(r4)
# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
# 内建的isinstance函数可以判断一个变量是不是字符串
L1 = ['Hello', 'World', 18, 'Apple', None]
r5 = [s.lower() for s in L1 if isinstance(s,str)]
print(r5)