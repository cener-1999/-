# -*-coding:utf-8-*-
import re
import jieba.analyse
import jieba
import wordcloud
from matplotlib import pyplot as plt

from createbales import *
from session import get_session

session=get_session()
results = session.query(Projects).all()
worddic={}

for result in results:
    text=result.name
    text = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",(result.name))
    jieba.analyse.set_stop_words("stopwords.txt")
    cuts=jieba.analyse.extract_tags(text)
    for cut in cuts:
        if(cut in worddic):
            worddic[cut]+=1
        else:
            worddic[cut]=1

ci = list(worddic.keys())
num = list(worddic.values())

data = []
for i in range(len(worddic)):
    data.append((num[i],ci[i]))

data.sort()
data.reverse()
print(data)


