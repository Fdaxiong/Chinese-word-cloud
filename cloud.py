import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 读取Text文本
data = open('小说.txt', "r", encoding="utf-8").read()
# 将文本已词语的方式分割 分割后赋值给Word
# ut_all=True 是全模式 cut_all=False 是精确模式 默认是精确模式
cutData = jieba.cut(data, cut_all=False)
# 以空格分开词语
word = " ".join(cutData)

# 背景图
mask = np.array(Image.open("masking.png"))

wc = WordCloud(mask=mask, font_path='HYXiXingKaiW.ttf', mode='RGBA', background_color='black').generate(word)

# 下面代码表示显示图片
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存图片
wc.to_file('cloud_img.png')
