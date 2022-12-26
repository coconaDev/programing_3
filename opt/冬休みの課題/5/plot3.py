import matplotlib.pyplot as plt
import japanize_matplotlib
temp = dict(); months = list()

temp[2018] = [17.2,16.9,19.9,21.6,25.6,27.8,28.3,28.5,28.4,23.9,23.1,20.4]
temp[2019] = [18.1,20.0,19.9,22.3,24.2,26.5,28.9,29.2,28.0,26.0,23.1,20.0]
temp[2020] = [18.7,18.7,20.1,19.8,24.8,28.1,29.3,29.4,27.7,25.8,23.4,19.2]
temp[2021] = [16.8,18.5,20.8,21.7,25.8,27.1,28.8,28.7,28.8,26.0,21.8,18.9]
temp[2022] = [17.7,17.2,20.4,22.7,23.5,27.0,29.4,29.9,28.3,26.0,23.6,19.4]

for i in range(1,13):
    months.append("%d月"%i)

# plotを重ねて呼び出す
plt.plot(months, temp[2018])
plt.plot(months, temp[2019])
plt.plot(months, temp[2020])
plt.plot(months, temp[2021])
plt.plot(months, temp[2022])

# 見た目を整える
plt.title("沖縄県の平均気温グラフ")
plt.xlabel('月'); plt.ylabel('気温[°C]')
plt.legend(["2018年","2019年","2020年","2021年","2022年"])
plt.axis(xmin=-0.5,xmax=11.5,ymin=15,ymax=35)
plt.grid()
plt.savefig("過去5年分の沖縄県の平均気温のグラフ.svg")
plt.show()