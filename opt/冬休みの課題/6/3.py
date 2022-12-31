# 2022年10月の陽性者数の推移と累積陽性者数を同時にプロット
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

x = []
progress = []
accumulation = []
sum = 0

data = pd.read_csv("陽性者数.csv", names=('data','vall')).values.tolist()
for i in range(183, 215):
    x.append(data[i][0])
    progress.append(data[i][1])
    accumulation.append(int(data[i][1])+int(sum))
    sum += data[i][1]


plt.plot(x,progress)
plt.plot(x,accumulation)
plt.title("2022年10月の陽性者数の推移と累積陽性者数")
plt.xlabel('月'); plt.ylabel('陽性者数（人）')
plt.xticks(['10月1日','10月10日','10月20日','10月30日'])
plt.legend(["陽性者数の推移",'累積陽性者数'])
plt.axis(xmin=0,xmax=len(x),ymin=0,ymax=900)
plt.savefig("2022年10月の陽性者数の推移と累積陽性者数.svg")
plt.show()


