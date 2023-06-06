def algae_count(counts):
    x = 1
    for i in range(counts-1):
        y = 3 * x
        x = x + y
    print("第%d周的水藻数量:%d" % (counts, x))


if __name__ == '__main__':
    count = int(input("请问你想知道第几周的水藻有多少颗？"))
    algae_count(count)
