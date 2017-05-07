# -*- coding: utf-8 -*-
import jieba.analyse

path = 'wangfeng.txt'
file_in = open(path, 'r')
content = file_in.read()

try:
    jieba.analyse.set_stop_words('tycb.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        #权重是小数，为了凑整，乘了一万
        print v + '\t' + str(int(n * 10000))

finally:
    file_in.close()