#!/usr/bin/env python3
import sys, io, cgi
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
if 'namae' in form:
    name = form['namae'].value
else:
    name = "名無し"

print ("Content-Type:text/html; charset=UTF-8\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>現在時刻</title>")
print("</head>")

print("<body>")
print("%sさんようこそ！"% name)
print("</body>")

print("</html>")
