def huiwen1():
    str = input("请输入：")
    if len(str) == 0:
        print("输入为空")
        str = input("请重新输入:")

    length = len(str)
    i = 0
    hw = 1
    while i <= (length/2):
        if str[i] == str[length-i-1]:
            hw = 1
            i = 1+i
        else:
            hw = 0
            break
    if hw == 1:
        print('是回文')
    else:
        print('不是回文')

def huiwen2():
    str1 = input("请输入：")
    if not str1:
        print("输入为空！")
        str1 = input("请重新输入：")
    str2 = reversed(list(str1))
    if list(str2) == list(str1):
        print("是回文")
    else:
        print("不是回文")