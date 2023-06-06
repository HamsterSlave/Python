from functools import reduce

#  定义函数square，用来计算一个数的平方
def  square(x):
        return  x  **  2

#  用map函数来对[1,2,3,4,5]中的每一个数调用square函数进行平方运算
r  =  map(square,[1,2,3,4,5])

#  打印map函数返回的对象r，在这里是一个迭代器对象
print(list(r))

#  将[1,2,3,4,5]的元素转换为字符串
r1  =  map(str,[1,2,3,4,5])
#  将map类型转换为list类型并打印输出
print(list(r1))


#  定义一个函数，接收两个参数  x  和  y
def  fn(x,  y):
        #  该函数返回  x  *  10  +  y  的结果
        return  x  *  10  +  y

#  定义一个函数，接收一个字符串作为参数  s
def  char2num(s):
        #  定义一个字典，每个数字字符  s  对应一个数字  digits[s]
        digits  =  {'0':  0,  '1':  1,  '2':  2,  '3':  3,  '4':  4,  '5':  5,  '6':  6,  '7':  7,  '8':  8,  '9':  9}
        #  函数返回  digits[s]  的值，即  s  字符对应的数字
        return  digits[s]

#  使用  map  函数将  char2num  应用到字符串  '13579'  的每个字符上，得到一个新的可迭代对象
#  再使用  reduce  函数按照  fn  函数指定的规则依次将可迭代对象的元素进行操作，最终得到一个结果
r3  =  reduce(fn,  map(char2num,  '13579'))
#  打印最终结果
print(r3)

def is_odd(n):
    return n % 2 == 1

r4 = filter(is_odd,[1,2,3,4,5])
print(list(r4))