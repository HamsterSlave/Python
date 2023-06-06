#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
#字典
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
# for value in d.values():
#     print(value)
# #字符串
# for i in 'ABCD':
#     print(i)
#下标
# for i,value in enumerate('ABCD'):
#     print(i,value)
# 两个变量
# for x,y in [(1,2),(3,5),(8,2)]:
#     print(x,y)
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    lens = len(L)
    if lens == 0:
        return (None, None)
    else:
        max = L[0]
        min = L[0]
        for i in range(len(L)):
            if L[i] >= max:
                max = L[i]
            if L[i] <= min:
                min = L[i]
        return (max,min)

max,min = findMinAndMax([1,2,2,7,4,8,76,0,4])
print(max,min)