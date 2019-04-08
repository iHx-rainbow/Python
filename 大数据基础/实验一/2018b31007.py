import pandas
import numpy


def temperature():
    f = input("请输入华氏温度：")
    c = 5/9*(int(f)-32)
    print("摄氏温度是：{:.2f}".format(c))

temperature()


def year():
    y = int(input("请输入年份："))
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print("是闰年")
    else:
        print("不是闰年")

year()


def number():
    # 用户输入数字
    num = int(input("请输入一个数字: "))

    # 质数大于 1
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "不是质数")
                print(i, "乘于", num//i, "是", num)
                break
            else:
                print(num, "是质数")

    # 如果输入的数字小于或等于 1，不是质数
    else:
        print(num, "不是质数")

number()


def salary():
    s = int(input("请输入利润（万元）："))
    if s <= 10:
        j = s*0.1
        print(j)
    elif s > 10 and s <= 20:
        j = 10*0.1+(s-10)*0.075
        print(j)
    elif s > 20 and s <= 40:
        j = 10*0.1+10*0.075+(s-20)*0.05
        print(j)
    elif s > 40 and s <= 60:
        j = 10*0.1+10*0.075+20*0.05+(s-40)*0.03
        print(j)
    elif s > 60 and s <= 100:
        j = 10*0.1+10*0.075+20*0.05+20*0.03+(s-60)*0.015
        print(j)
    elif s > 100:
        j = 10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(s-100)*0.01
        print(j)

salary()


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("请输入斐波那契(Fibonacci)数列位："))
# for n in range(1,10):
print(fibo(n))


def np():
    a = numpy.random.randint(0, 20, (4, 4))
    b = numpy.arange(0, 31, 2).reshape(4, 4)
    print(a)
    print(b)
    c = numpy.dot(a, b)
    print(c)

np()

def info():
    csv = open(r'大数据基础\data\food_info.csv')
    food_info = pandas.read_csv(csv)    # read_csv方法不能使用有中文的参数
    k_mean = food_info["Energ_Kcal"].mean()
    k_max = food_info["Energ_Kcal"].max()
    print("平均值是{:.2f}，最大值是{}".format(k_mean, k_max))
    weighted_protein = food_info["Protein_(g)"]*2
    weighted_fat = -0.75*food_info["Lipid_Tot_(g)"]
    initial_rating = weighted_protein*weighted_fat
    print("Score is:", initial_rating.std())

info()