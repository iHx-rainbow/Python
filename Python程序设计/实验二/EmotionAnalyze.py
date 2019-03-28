import jieba
import re


def split(sentence):  # 传入句子，返回分词列表和感叹号出现次数
    pattern = '。|，|？|！'
    wordslist = []
    t = sentence.count("！")
    sentence = sentence.strip()
    juzi_list = re.split(pattern, sentence)
    while '' in juzi_list:
        juzi_list.remove('')
    for juzi in juzi_list:
        wordslist = wordslist+jieba.lcut(juzi)
    return wordslist, t


def count(wordslist):  # 传入分词列表，返回褒义词贬义词的出现次数p和n
    p, n = 0, 0
    for word in wordslist:
        p = polist.count(word)+p
    for word in wordslist:
        n = nelist.count(word)+n
    return p, n


fo = open("Text.txt", "r")
# print ("文件名为: ", fo.name)
textlist = fo.readlines()
duanlist = []
# i = 1
for duan in textlist:  # 依次读取每行
    duan = duan.strip()  # 去掉每行头尾空白
    # print("第%d段为: %s" % (i, duan))
    # i = i+1
    duanlist.append(duan)
positive = open(
    r".\sentiment.dict.v1.0\tsinghua.positive.gb.txt", "r").readlines()
negative = open(
    r".\sentiment.dict.v1.0\tsinghua.negative.gb.txt", "r").readlines()
polist = []
nelist = []
for word in positive:
    word = word.strip()
    polist.append(word)
# print(polist)
for word in negative:
    word = word.strip()
    nelist.append(word)
# print(polist)
fo.close()  # 关闭文件

for sentence in duanlist:
    wordslist, t = split(sentence)
    p, n = count(wordslist)
    print(' {}感叹号出现次数：{} 褒义词次数：{} 贬义词次数：{}'.format(wordslist,t,p,n))
