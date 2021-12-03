import random
from matplotlib import font_manager
from matplotlib import pyplot as plt
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
x = range(0,120)
y = [random.randint(20,35) for i in range(120)]
plt.figure(figsize=(20,8),dpi=80, fontproperties=my_font)




plt.plot(x,y)
plt.show()
# from sklearn.datasets import make_blobs, load_iris
# import matplotlib.pyplot as plt
#
# # 支持中文
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#
# n_samples = 1500
# random_state = 170
# x, y = make_blobs(n_samples=n_samples, random_state=random_state)
# # x, y = load_iris(True) # 莺尾花
# print(x.shape, y.shape)
# plt.scatter(x[:, 0], x[:, 1], c=y)
# plt.title(u"原始数据分布")
# plt.show()
