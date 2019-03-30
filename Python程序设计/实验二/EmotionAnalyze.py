import jieba
import re


def split(sentence):  # 传入句子，返回分词列表wordslist和感叹号出现次数t
    pattern = '。|，|？'
    wordslist = []
    #t = sentence.count("！")
    sentence = sentence.strip()
    juzi_list = re.split(pattern, sentence)
    while '' in juzi_list:
        juzi_list.remove('')
    for juzi in juzi_list:
        wordslist = wordslist+jieba.lcut(juzi)
    return wordslist


def count(wordslist):  # 传入分词列表，返回褒义值p和贬义值n
    p, n = 0, 0
    chengdu = ['很', '非常', '极度', '无比', '太']
    fouding = ['不', '没有']
    for index in range(len(wordslist)):
        for poword in polist:

            if wordslist[index] == poword:
                if fouding.count(wordslist[index-1]) != 0:  # 否定反转
                    if chengdu.count(wordslist[index-2]) != 0:  # 否定反转加程度
                        n = n+2
                    else:
                        n = n+1

                elif chengdu.count(wordslist[index-1]) != 0:  # 程度判断
                    p = p+2

                else:
                    p = p+1

        #p = polist.count(word)+p

        for neword in nelist:

            if wordslist[index] == neword:
                if fouding.count(wordslist[index-1]) != 0:  # 否定反转
                    if chengdu.count(wordslist[index-2]) != 0:  # 否定反转加程度
                        p = p+2
                    else:
                        p = p+1

                elif chengdu.count(wordslist[index-1]) != 0:  # 程度判断
                    n = n+2

                else:
                    n = n+1

        #n = nelist.count(word)+n

    t = wordslist.count("！")+1  # 感叹语气
    p = p*t
    n = n*t
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
    wordslist = split(sentence)
    p, n = count(wordslist)
    while '！' in wordslist:
        wordslist.remove('！')
    print('{}  褒义度：{} 贬义度：{}'.format(wordslist, p, n))
