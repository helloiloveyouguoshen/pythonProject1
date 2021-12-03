from matplotlib import pyplot as plt
from matplotlib import font_manager

y_3 = [11,5,5,22,33,11,54,15,12,3,6,12,45,65,4,12,4,5,1,2,45,15,24,4,4,1,15,12,14,12,16]
y_10 = [11,7,4,5,7,5,4,5,5,5,4,4,5,4,1,1,2,4,4,1,1,13,4,1,4,15,11,11,15,14,12]
x_3 = range(1,32)
x_10 = range(51,82)


# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#使用scatter绘制散点图，和之前绘制折线图的唯一区别
plt.scatter(x_3,y_3,label="3月份")
plt.scatter(x_10,y_10,label="10月份")
plt.rcParams['font.sans-serif'] = ['FangSong']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False
#调整x刻度
_x = list(x_3)+list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45)

# 添加图例
plt.legend(loc="upper left")
plt.xlabel("时间",color='red')
plt.ylabel("温度")
plt.title("三月和十月气温表",color='#EE82EE')
plt.show()