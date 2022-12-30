#!/usr/bin/env python3
import sys, io, cgi

teihen,takasa = 0,0
form = cgi.FieldStorage()

if 'teihen' in form:
    teihen = int(form['teihen'].value)
if 'takasa' in form:
    takasa = int(form['takasa'].value)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print ("Content-Type:text/html; charset=UTF-8\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>面積</title>")
print("</head>")

print("<body>")
print("<p>底辺：%d</p>" % teihen)
print("<p>高さ：%d</p>" % takasa)
print("<p>面積：%d × %d / 2 = %d</p>" %(teihen, takasa, teihen*takasa/2) )
print("</body>")

print("</html>")
