from wordcloud import WordCloud
from matplotlib import rc
import matplotlib.pyplot as plt

with open('댓글.csv', encoding='UTF-8') as file:
    text = file.read()

file.close()

rc('font', family='NanumGothic')

wcloud = WordCloud('./data/D2Coding.ttf',
                   max_words=1000,
                   relative_scaling=0.2).generate(text)

plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis('off')
plt.show()