#!/usr/bin/env python3
import sys
import io
from datetime import datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print ("Content-Type:text/html; charset=UTF-8\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>現在時刻</title>")
print("</head>")

print("<body>")
print("<p>現在時刻： %s</p>" % datetime.now().strftime("%H:%M:%S"));
print("</body>")

print("</html>")
