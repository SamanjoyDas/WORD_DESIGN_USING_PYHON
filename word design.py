from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = '''Enter your message here for the plot.'''

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
