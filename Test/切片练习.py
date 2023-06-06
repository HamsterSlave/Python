L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
for i in range(len(L)-2):
    r.append(L[i])
print(r)
r1 = L[:3]
print(r1)
r2 = L[1:3]
print(r2)
r3 = L[-1:]
print(r3)
r4 = L[-2:-1]
print(r4)

r4 = (1,2,3,4,5,6,7,8,9,0)[-3:]
print(r4)

r5 = 'ABCDEFG'[:3]
print(r5)