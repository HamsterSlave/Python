# for i in range(3):
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     if name == "sevn" or "alex" and password == "123":
#         print("登录成功！")
#         break
#     else:
#         print("登录失败！")
i = 2
even  = []
odd  = []
while i<=100:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
    i += 1
print(even)
print(odd)