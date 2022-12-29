#!/usr/bin/env python3
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print ("Content-type:text/html; charset=UTF-8\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>テスト　CGI</title>")
print("</head>")

print("<body>")
print("<h1>Hello CGI World!</h1>");
print("<h2>日本語の表示はうまくいくかな？</h2>");
print("</body>")

print("</html>")