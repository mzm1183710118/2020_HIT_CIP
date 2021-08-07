# -*- coding: utf-8 -*-
from __future__ import division
import linecache
import jieba


def getTrueAnswer(inPath, outPath):
    fR = open(inPath, 'r', encoding='UTF-8')

    sent = fR.read()
    sent_list = jieba.cut(sent)

    fW = open(outPath, 'w', encoding='UTF-8')
    fW.write(' '.join(sent_list))

    fR.close()
    fW.close()


def accuracy(myAnswer, trueAnswer):
    r1 = open(myAnswer, 'r', encoding='utf-8')
    # 记录总的行数，即句子数
    r1_len = len(r1.readlines())
    # 循环计数器
    count = 1
    # 分词正确的句子数目
    num = 0
    while True:
        if count > r1_len:
            break
        # 截取我的答案的对应行内容
        content1 = linecache.getline(myAnswer, count)
        # 截取正确答案的对应行内容
        content2 = linecache.getline(trueAnswer, count)
        # 若二者相同则将正确分词的句子数目+1
        if content1.strip() == content2.strip():
            num += 1
        count += 1

    result = num / r1_len
    return result
