# !/usr/bin/env python3
import sys, io, cgi
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

if 'name' in form:
    name = form['name'].value
else:
    name = '名無し'

if 'age' in form:
    age = form['age'].value
else:
    age = "年齢不詳"

if 'class' in form:
    clas= form['class'].value

print ("Content-Type:text/html; charset=UTF-8\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>データ入力</title>")
print("</head>")

print("<body>")
print("<p>名前　%s</p>" % name)
print("<p>年齢　%s</p>" % age)
print("<p>学科：%s</p>" % clas)
print("</body>")

print("</html>")
