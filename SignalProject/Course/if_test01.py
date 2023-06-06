height = 1.75
weight = 80.5
bmi = weight/(height ** 2)
print(bmi)
if bmi<=18.5:
    print('过轻')

if 18.5<bmi<=25:
    print('正常')

if 25<bmi<=28:
    print('过重')

if 28<bmi<=32:
    print('肥胖')

if bmi>32:
    print('严重肥胖')