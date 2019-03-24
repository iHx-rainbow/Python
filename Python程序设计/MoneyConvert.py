# 1美元=6人民币
Moneystr = input("人民币请用元或￥结尾，美元用$符号结尾\n请输入带有符号的货币值：")
if Moneystr[-1] in ['元', '￥']:
    dollar = eval(Moneystr[0:-1])*6
    print("转换后的货币是{:.2f}美元".format(dollar))
elif Moneystr[-1] in ['$']:
    rmb = eval(Moneystr[0:-1])/6
    print("转换后的货币是{:.2f}人民币".format(rmb))
else:
    print("输入格式错误！")
