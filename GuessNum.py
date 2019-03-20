import numpy
print("猜数游戏")
a = numpy.random.randint(0, 100)
# print(a)
try:
    b = int(input("请输入一个0-100之间的整数："))
    i = 0
    while a != b:
        if a < b:
            print("遗憾，太大了")
            b = int(input("请输入一个0-100之间的整数："))
            i = i+1
        else:
            print("遗憾，太小了")
            b = int(input("请输入一个0-100之间的整数："))
            i = i+1
    else:
        i = i+1
        print("预测{}次，你猜中了！".format(i))

except ValueError:
    print("输入内容必须为整数！")
