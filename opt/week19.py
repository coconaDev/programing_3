import re

p = re.compile(^[\d]{4})-([\d]{1,2})-([\d]{1,2})$)

while True:
    s = input()
    a = p.search(s)

    year = int(a.group(1))
    month = int(a.group(2))
    day = int(a.group(3))

    if :
        print("")
    else:
        print("日付ではありません")