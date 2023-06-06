day = 1
while day <=7:
    answer = input("你有好好学习吗？")
    if answer != "有":
        
        break
    day += 1
else:
    print("恭喜你，已经连续7天坚持学习！")
