#!/usr/bin/env python3
import sys
import io
from datetime import datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print ("Content-type:text/html; charset=UTF-8\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>ただいまの日時</title>")
print("</head>")

print("<body>")
print("<p>ただいまの日時： %s</p>" % datetime.now().strftime("%Y/%m/%d %H:%M:%S"));
print("</body>")

print("</html>")