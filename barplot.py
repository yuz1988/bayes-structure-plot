from matplotlib import pyplot as plt

plt.figure(figsize=(8, 5))
labels = ['Building Graph \n (include edge weight \n computation)',
          'Building Tree \n (include direction)', 'Building BayesNet \n (learn parameters)']
legend_labels = ['Building Graph', 'Building Tree', 'Building BayesNet']
sizes = [2.6204, 0.1784, 0.0094]
colors = ['red', 'blue', 'green']

patches, l_text, p_text = plt.pie(sizes, labels=labels, colors=colors,
                                  labeldistance=1.2, autopct='%3.1f%%', shadow=False,
                                  startangle=180, pctdistance=0.6)

# labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
# autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
# shadow，饼是否有阴影
# startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
# pctdistance，百分比的text离圆心的距离
# patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

# 改变文本的大小
# 方法是把每一个text遍历。调用set_size方法设置它的属性
for t in l_text:
    t.set_size = (50, )
for t in p_text:
    t.set_size = (50, )
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.legend(legend_labels)
plt.savefig('barplot.png')
