## python 个性化中文词云

制作"词云"是今天的主题

词云可以很直观的看出来里面的的词语出现的最多次

词云可以用于数据分析,也可以给用户群体打标签

最后的成品:

![](https://github.com/Fdaxiong/Chinese-word-cloud/blob/master/cloud_img.png)



"""
1.安装好这些库并导入
    import jieba
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import numpy as np
    from PIL import Image
这里我已pyCharm为列安装
在控制台右下角有一个Terminal 点击进去
输入指令 pip install 库的名字 回车等待安装即可

也可以直接写入代码,会报错,然后光标移到报错地址按快捷键 Alt+Enter会出现 install 安装 点击安装就好了
pyCharm小技巧 快速导包快捷键 Alt+Enter+Enter 

2.准备好一个TXT.文本
    TXT文本里面要有文字内容

![](https://github.com/Fdaxiong/Chinese-word-cloud/blob/master/小说.png)


3.准备一张图片jpg.png格式都可用 
    这里的图片是作为词云的蒙版使用
    (个性化词云就是因为背景图蒙版不一样)

![](https://github.com/Fdaxiong/word-cloud/blob/master/masking.png)

4.还要准备好一个字体.
    HYXiXingKaiW.ttf
    字体在哪里找? 字体后缀名是.TTR
    一般在电脑的系统盘:这是我电脑字体存放的路径  C:\Windows\Fonts
    进去里面复制一个你喜欢的字体出来

![](https://github.com/Fdaxiong/Chinese-word-cloud/blob/master/字体.png)

5.以上文本,图片,字体我都存放在同一个文件夹下
         准备好这些就可以编写代码了
"""

```python
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


'''
WordCloud()可选的参数
font_path：可用于指定字体路径，包括otf和ttf
width：词云的宽度，默认为400
height：词云的高度，默认为200
mask：蒙版，可用于定制词云的形状
min_font_size：最小字号，默认为4
max_font_size：最大字号，默认为词云的高度
max_words：词的最大数量，默认为200
stopwords：将被忽略的停用词，如果不指定则使用默认的停用词词库
background_color：背景颜色，默认为black
mode：默认为RGB模式，如果为RGBA模式且background_color设为None，则背景将透明
'''

wc = WordCloud(mask=mask, font_path='HYXiXingKaiW.ttf', mode='RGBA', background_color='black').generate(word)

# 下面代码表示显示图片
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存图片
wc.to_file('cloud_img.png')

```





