from matplotlib import pyplot as plt
from matplotlib import font_manager

if __name__ == "__main__":
    font = font_manager.FontProperties(fname='C:/Windows/fonts/simkai.ttf')

    a = ["猩球崛起:终极之战","敦刻尔克","蜘蛛侠:英雄归来","战狼2"]

    b_16 = [15746,312,4997,319]
    b_15 = [12357,156,2045,168]
    b_14 = [2358,399,2358,362]

    bar_width=0.2

    #重点，x轴右移
    x_14 = list(range(len(a)))
    x_15 = [i+bar_width for i in x_14]
    x_16 = [i+bar_width*2 for i in x_14]

    #设置图形大小像素
    plt.figure(figsize=(10,5))

    # 绘制条形图
    plt.bar(range(len(a)),b_14,width=bar_width,label="9月14日")
    plt.bar(x_15, b_15,  width=bar_width,label="9月15日")
    plt.bar(x_16, b_16,  width=bar_width,label="9月16日")

    #设置x轴刻度
    plt.xticks(x_15,a,fontproperties="KaiTi")

    #设置图例
    plt.legend(prop=font)

    plt.xlabel("电影名称",fontproperties="KaiTi",size=20)
    plt.ylabel("票房情况", fontproperties="KaiTi", size=20)
    plt.title("票房随时间的变化", fontproperties="KaiTi", size=30)


    plt.show()
