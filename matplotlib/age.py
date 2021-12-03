from matplotlib import pyplot as plt
from matplotlib import font_manager
# my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
y1 = [1,5,2,1,2,4,4,8,8,4,1,1,5,5,1,2,1,4,1,4]
y2 = [1,1,1,5,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1]
x = range(11,31)
plt.figure(figsize=(10,4),dpi=80)
plt.plot(x,y1,label="自己",color="orange",linestyle=':',linewidth=2)
plt.plot(x,y2,label="同桌",color="cyan")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False
_xtick_labels = ["{}岁".format(i) for i in x]
# plt.xticks(x,_xtick_labels,fontproperties=my_font)
# plt.yticks(range(0,8))
plt.xticks(x,_xtick_labels)
# 添加图例
plt.legend(loc="upper left")
# 绘制网格
plt.grid(alpha=0.4,linestyle='--')

plt.show()