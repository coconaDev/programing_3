# excelに出力するプログラム
import requests, bs4, re
import openpyxl, glob
import matplotlib.pyplot as plt
import japanize_matplotlib

temp = {}

def main():
    web()
    excel()
    graph()

def web():
    # 那覇の気温を取得
    url1 = "https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php"\
    "?prec_no=91&block_no=47936&year=2022&month=&day=&view="

    # requests.getでWebページを取得
    res = requests.get(url1)
    soup = bs4.BeautifulSoup(res.content,'html.parser')

    for i in range(0,133):
        # 1890年~2022年分回す
        elements = soup.select('table')[3].select('tr')[i+1]

        if (elements.select('td')[13].text == '×') or (elements.select('td')[13].text == '\u3000' ) or (re.search("]",elements.select('td')[13].text)):
            # X \u3000 ] はNoneで埋める
            temp.setdefault(int(elements.select('a')[0].text),[]).append(None)
        else:
            temp.setdefault(int(elements.select('a')[0].text),[]).append(float(elements.select('td')[13].text))


    # 名護の気温を取得
    url2= "https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?"\
    "prec_no=91&block_no=47940&year=2022&month=&day=&view="
    res = requests.get(url2)
    soup = bs4.BeautifulSoup(res.content,'html.parser')
    for i in range(0,57):
        elements = soup.select('table')[3].select('tr')[i+1]
        if (elements.select('td')[13].text == '×') or (elements.select('td')[13].text == '\u3000' ) or (re.search("]",elements.select('td')[13].text)):
            temp.setdefault(int(elements.select('a')[0].text),[]).append(None)
        else:
            temp.setdefault(int(elements.select('a')[0].text),[]).append(float(elements.select('td')[13].text))
    # 欠損値の補完
    for i in range(1890, 1966):
        temp[i].append(None)

    return 0

def excel():
    wb = openpyxl.load_workbook("temp.xlsx")
    sheet = wb.active

    sheet['B1'] = '那覇'
    sheet['C1'] = '名護'

    for i in range(0,132):
        # 年
        sheet[format(chr(65)+str(i+2))] = i + 1890
        # 那覇
        sheet[format(chr(66)+str(i+2))] = temp[i+1890][0]
        # 名護
        sheet[format(chr(67)+str(i+2))] = temp[i+1890][1]


    # 小数点第１位まで表示
    for row in sheet.iter_cols():
        for cell in row:
            if (cell.col_idx == 2) or (cell.col_idx == 2):
                cell.number_format = "0.0"

    wb.save('temp.xlsx')
    glob.glob("*.xlsx")

    return 0

def graph():
    year = list(temp.keys())
    # 那覇と名護の値を分割 
    val = list(temp.values())
    naha = []
    nago = []
    for i in range(0,133):
        naha.append(val[i][0])
        nago.append(val[i][1])

    # plotを重ねて呼び出す
    plt.plot(year, naha)
    plt.plot(year, nago)

    # 見た目を整える
    plt.title("観測開始時から年ごとの気温のグラフ")
    plt.xlabel('年'); plt.ylabel('気温[°C]')
    plt.legend(["那覇","名護"])
    plt.axis(xmin=1885,xmax=2025,ymin=20.0,ymax=25.0)
    plt.savefig("temp.svg")
    plt.show()

if __name__ == "__main__":
    main()