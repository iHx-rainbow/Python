#计算验证调和级数并非收敛
m = int(input("请输入最大调和级数项数："))
a=0
for n in range(1,m+1):
    a=1/n+a
    print(a)
    pass