#coding:gbk
'''
人物关系
谢钦豪
'''
import codecs
import jieba.posseg as pseg
import jieba

names = {}#  保存人物
relationships = {}#保存人物关系的有向边，
lineNames = []# 缓存人物名称
jieba.load_userdict("names.txt")#加载人物表
with open("黎明破晓的街道.txt", 'r', encoding='gbk') as f:
    for line in f.readlines():
        poss = pseg.cut(line)  
        lineNames.append([])  
        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue
            lineNames[-1].append(w.word) # 为当前段的环境增加一个人物
            if names.get(w.word) is None: 
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1 # 输出人物出现次数统计结果

for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1
with codecs.open("People_node.csv", "w", "gbk") as f:
    f.write("ID,Label,Weight\n")
    for name, times in names.items():
        if times > 10:
            f.write(name + "," + name + "," + str(times) + "\n")
with codecs.open("People_edge.csv", "w", "gbk") as f:
    f.write("Source,Target,Weight\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + "," + v + "," + str(w) + "\n")
