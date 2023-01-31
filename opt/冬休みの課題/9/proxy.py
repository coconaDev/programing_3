import requests
import bs4
from bs4 import BeautifulSoup
proxies = {
  'http':'http://cproxy.okinawa-ct.ac.jp:8080',
  'https':'http://cproxy.okinawa-ct.ac.jp:8080',
}

temps = {}

# 末尾に￥をつけると複数行に分けて記述できる
url = "https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php"\
"?prec_no=91&block_no=47936&year=2022&"\
"month="\
"&day="\
"&view="


# requests.getでWebページを取得
res = requests.get(url, proxies=proxies)

soup = bs4.BeautifulSoup(res.content,'html.parser')

for i in range(0,132):
    elements = soup.select('table')[3].select('tr')[i+1]
    temp = [None]*12

    for j in range(1,13):
        if (elements.select('td')[j].text == '×') or (elements.select('td')[j].text == '\u3000' ):
            temp[j-1] = None
        else:
            temp[j-1] = elements.select('td')[j].text

    temps.setdefault(elements.select('a')[0].text,[]).append(temp)
print(temps)
