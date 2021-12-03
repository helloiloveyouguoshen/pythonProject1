
from matplotlib import pyplot as plt

import matplotlib
font = {
    'family':'SimHei',
    'weight':'bold',
    'size':12
}
matplotlib.rc("font", **font)

a = ["流浪地球","复仇者联盟4:终局之战","哪吒之魔童降世","疯狂的外星人","飞驰人生","蜘蛛侠:英雄远征","扫毒2天地对决","烈火英雄","大黄蜂","惊奇队长","比悲伤更悲伤的故事","哥斯拉2:怪兽之王","阿丽塔:战斗天使","银河补习班","狮子王","反贪风暴4","熊出没","大侦探皮卡丘","新喜剧之王","使徒行者2:谍影行动","千与千寻"]
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23,5.22]

#设置图片大小
plt.figure(figsize=(14,8),dpi=80)
#绘制条形图
# plt.bar(a,b)
#绘制横的条形图
plt.barh(range(len(a)),b,height=0.5,color="red")
#设置刻度及刻度标签

plt.yticks(range(len(a)),a)
# 绘制网格
plt.grid(alpha=0.4,linestyle='--',color="green")
plt.show()
