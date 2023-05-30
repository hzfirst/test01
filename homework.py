# 1
# 用户输入年龄，如果年龄超过65岁，输出："可以退休了"，
# 否则，输出："小伙子，加油干！"

# age = int(input("请输入您的年龄："))
# if age >= 65:
#     print("可以退休了！")
# else:
#     print("小伙子，加油干！")

# 2
# 用户输入年龄，按照如下标准书写程序，判断用户处于哪个年龄阶段，
# 并提示：您的年龄是xx: 青少年/青年/中年/老年。
# 年龄段划分标准：0-17岁为青少年；18-35岁为青年；36-59为中年，60-99岁为老年。

# age = int(input("请输入您的年龄："))
# if 60 <= age <= 99:
#     print("老年")
# elif 36 <= age <= 59:
#     print("中年")
# elif 18 <= age <= 35:
#     print("青年")
# else:
#     print("青少年")

# 3
# 制作用户登录系统：已知A用户注册的用户名为`aaa`，密码是`123456`。具体要求如下：
#
# 登录时需要验证用户名、密码、验证码(固定验证码为`qwer`)。
#
# 提示：系统先验证验证码是否正确，正确后再验证用户名和密码。

# 用户名和用户密码
#
# A_user = "aaa"
# password = "123456"
# verify = "qwer"
# User = input("请输入用户名：")
# Password = input("请输入用户密码：")
# Verify = input("请输入验证码：")
#
# if Verify == verify:
#     if User == A_user and password == Password:
#         print("登录成功！")
#     else:
#         print("您输入的用户名或密码有误！")
# else:
#     print("验证码有误！")

# 4
# - 1-7七个数字，分别代表周一到周日，
# - 如果输入的数字是6或7，输出“周末”，否则输出“工作日”

# wook = int(input("请输入1~7(1到7表示：周一到周日)："))
# if wook == 7 or wook == 6:
#     print("周末")
# else:
#     print("工作日")

# 5
# - 1-7七个数字，分别代表周一到周日，
# - 如果输入的数字是1，输出“今天是周一”
# - 如果输入的数字是2，输出“今天是周二”
# - 如果输入的数字是3，输出“今天是周三”
# - 如果输入的数字是4，输出“今天是周四”
# - 如果输入的数字是5，输出“今天是周五”
# - 如果输入的数字是6或7，输出“今天是周末”

# wook = int(input("请输入1~7(1到7表示：周一到周日)："))
# if wook == 1:
#     print("周一")
# elif wook ==2:
#     print("周二")
# elif wook ==3:
#     print("周三")
# elif wook ==4:
#     print("周四")
# elif wook ==5:
#     print("周五")
# elif wook ==6:
#     print("周六")
# else:
#     print("周日")

# 6
# 闰年判断程序(闰年是能被4整除，但不能被100整除的；或者能被400整除的年份)
#
# 输入一个有效的年份，判断是不是闰年
#
# 如果是闰年，则打印“xxxx年是闰年”；否则打印“xxxx年不是闰年”
#
# 如输入"2018"，将打印“2018年不是闰年”

# year = int(input("请输入年份："))
#
# if year < 0:
#     print("您输入的年份有误！")
# else:
#     if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
#         print(f"{year}是闰年！")
#     else:
#         print(f"{year}年不是闰年!")

# 7
# 1. 书写代码求 0-100之间所有数字的累加和
#
# 2. 书写代码求 0-100 之间偶数的累加和

# sum = 0
# for x in range(0,101):
#     sum+=x
# print(f"0-100之间所有数字的累加和是{sum}")

# sum = 0
# for x in range(0,101,2):
#     sum+=x
# print(f"0-100之间所有数字的累加和是{sum}")

# 8
# 请输出第一个数字:
# 请输入第二个数字:
# 请输入要进行的操作(+ - * /):
# 计算的结果为:
# 举例如下:
# 请输出第一个数字: 10
# 请输入第二个数字: 20
# 请输入要进行的操作(+ - * /): +
# 计算的结果为: 10 + 20 = 30

# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))
# symbol = input("请输入(+ - * /)：")
# result = 0
# if symbol == "+":
#     print(f"{num1} + {num2} =", num1+num2)
# elif symbol == "-":
#     print(f"{num1} - {num2} =", num1-num2)
# elif symbol == "*":
#     print(f"{num1} * {num2} =", num1*num2)
# else:
#     print(f"{num1} / {num2} =", num1/num2)

# 9
# 1. 电脑产生一个（1-100）的随机数，用户进行猜测(通过 input 输入)，直到猜中为止。
# 2. 如果猜对了，输出：恭喜你猜对了，数字是 xx。
# 3. 如果猜的数字比随机数大，输出：猜测的数字太大了，继续加油
# 4. 如果猜测的数字比随机数小，输出：猜测的数字有点小，再来一次

# 根据需求写出每一步：

# 电脑产生随机数
# import random
# pc_num = random.randint(1,100)
# while True:
#     # 用户输入数值
#     u_num = int(input("请输入一个数:"))
#     # 猜对直接跳出循环体
#     if u_num == pc_num:
#         print(f"恭喜你猜对了，数字是{pc_num}")
#         break
#     # 如果猜的数字比随机数大，输出：猜测的数字太大了，继续加油
#     elif u_num > pc_num:
#         print("猜测的数字太大了，继续加油!")
#     # 如果猜测的数字比随机数小，输出：猜测的数字有点小，再来一次
#     elif u_num < pc_num:
#         print("猜测的数字有点小，再来一次")



# 10
"""
需求:
 1. 提示用户输入登录系统的用户名和密码
 2. 校验用户名和密码是否正确(正确的用户名:admin、密码:123456)
 3. 如果用户名和密码都正确，打印“登录成功!”，并结束程序
 4. 如果用户名或密码错误，打印“用户名或密码错误!”，提示用户继续输入用户名和密码登录
 5. 如果用户输入的用户名为“exit”，则退出程序
"""
# 本地的用户数据
local_name = "admin"
local_password = 123456

while True:
    # 用户录入用户名
    name = input("请输入用户名：")
    # 用户输入的用户名为“exit”，则退出程序
    if name == "exit":
        break
    # 输入账号的密码
    password = eval(input("请输入密码："))
    # 校验用户名和密码是否正确
    if name == local_name and password == local_password:
        print("登录成功！")
        break
    else:
        print("用户名或密码错误!")



