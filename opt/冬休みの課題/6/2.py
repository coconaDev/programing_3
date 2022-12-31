# 2022年4月1日から11月31日までの累積陽性者数
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

x = []
y = []
sum = 0

data = pd.read_csv("陽性者数.csv", names=('data','vall')).values.tolist()
for i in range(0, len(data)):
    x.append(data[i][0])
    y.append(int(data[i][1])+int(sum))
    sum += data[i][1]


plt.plot(x,y)
plt.title("2022年4月1日から11月31日までの累積陽性者数")
plt.xlabel('月'); plt.ylabel('陽性者数（人）')
plt.xticks(['4月1日','5月1日','6月1日','7月1日','8月1日','9月1日','10月1日','11月1日'])
plt.axis(xmin=-1,xmax=len(x),ymin=0,ymax=3800)
plt.savefig("2022年4月1日から11月31日までの累積陽性者数.svg")
plt.show()


