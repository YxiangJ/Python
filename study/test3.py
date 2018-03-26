# 人狗年龄对比系统
print("======人狗年龄对比系统======")
while True:
    try:
        age=int(input("请输入狗狗的年龄："))
        print("")
        age=float(age)
        if age<0:
            print("Are you kidding me?")
        elif age==1:
            print("相当于人类14岁")
            break
        elif age==2:
            print("相当于人类22岁")
            break
        else:
            human=22+(age-2)*5
            print("相当于人类:",human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄。")

input("点击enter退出")
