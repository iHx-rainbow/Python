import numpy
import pandas as pd
import os
import easygui as g
import xlrd
 
 
 
 
 
path = g.fileopenbox(msg="选择文件", title="选择要查询的文件清单", default='*', filetypes=None)
data = xlrd.open_workbook(path, encoding_override='utf-8')    #打开文件（文件路径）
table = data.sheets()[0]  # 选定表    #第一个工作簿
nrows = table.nrows  # 获取行号
ncols = table.ncols  # 获取列号
names = []   #空列表存储
for i in range(1, nrows):  # 第0行为表头
    alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
    name = alldata[0]  # 取出表中第二列数据
    names.append(name)
print('要查询的信息如下：')
print(names)
 
 
def listdir(path, path_name):  # 定义传入存储文件的list函数
    for file in os.listdir(path):    #依次获得返回指定的文件夹包含的文件或文件夹的名字的列表
        file_path = os.path.join(path, file)    #将多个路径组合后返回
        if os.path.isdir(file_path):    #返回一个列表，其中包含有指定路径下的目录和文件的名称
            listdir(file_path, path_name)
        else:
            path_name.append(file_path)       #加入到路径列表中
 
 
path_name = []
path = g.diropenbox(msg="请选择文件夹", title="选择要查询的文件夹")
listdir(path,path_name)
 
 
for path in path_name:
    file = os.path.split(path)   #拆分分隔符
    file_name = file[1]
 
 
 
    try:
        data = pd.read_excel(path,None)     #读取待查询的excel文件数据,设置None可以生成一个字典，字典中的key值即为sheet名字
        sheet_names = []    #用一个空列表， 准备存储sheet的名字
        for sh_name in data.keys():    #依次便利data.key（）中的名字
            # print(sh_name)
            sheet_names.append(sh_name)    #将sheet名字存储进入列表sheet_names
        for sheet_name in sheet_names:    #依次循环获得工作簿
            workbook = pd.read_excel(path, sheet_name=sheet_name)  # 文件路径和sheet名字
            # print(workbook)
            for indexs in workbook.index:  # 用.index进行依次查找
                for i in range(len(workbook.loc[indexs].values)):  # 依次生成
                    for name in names:    #依次循环
                        if (workbook.loc[indexs].values[i] == name):    #如果查找到该关键词
                            print("*" * 50)
                            print("[" + name + "]的位置在" + path + "  的" + sheet_name + "   工作簿中")    #显示位置
                            print('行数：', indexs + 1, '列数：', i + 1)    #行数和列数，从0开始，要加1
                            print("*" * 50)
                            data = pd.DataFrame(pd.read_excel(path,sheet_name=sheet_name))  # 读取数据,设置None可以生成一个字典，字典中的key值即为sheet名字，此时不用使用DataFram，会报错
                            counts = data.loc[indexs]
                            print("[" + name + "]所在行数据如下：")
                            print(counts)  # 获取行名为0这一行的内容
                            df = pd.DataFrame(counts)
                            print(df)
                            file_save_name ='[' + name + ']-在文件[' + file_name + ']中的['+ sheet_name +']工作簿中的行数据'    #关键词所在位置
                            with open(name + '.txt', 'a+',encoding='utf-8') as f:  # 用w格式新建文件，并且用file_name命名，再加上“.txt”后缀，文字编码格式'utf-8'
                                f.write(file_save_name + '\n')  # 将文件位置写入到文本
                                f.close()  # 将文件关闭保存
                            df.to_excel(file_save_name + ".xlsx")   #写入文件
 
    except Exception as e:
        print(e)
        pass
 
print("自动查询和生成完毕")