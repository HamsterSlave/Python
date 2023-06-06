#在循环的过程中不断推算出列表后续的元素
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x*x for x in range(1,11))
for n in g:
    print(n)
# 类似列表生成式的for循环无法实现的时候，还可以用函数来实现
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)