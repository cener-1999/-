# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import jieba

text = ""
with open("alice.txt", "r+") as file:
    text = file.read()
    pass

wd = WordCloud(max_words=50, background_color="white").generate(text)

plt.figure()
plt.imshow(wd, interpolation="bilinear")
plt.axis("off")
plt.show()

mask = np.array(Image.open('alice_mask.png'))
wd = WordCloud(max_words=500, background_color="white", mask=mask).generate(text)

plt.figure()
plt.imshow(wd, interpolation="bilinear")
plt.axis("off")
plt.show()
