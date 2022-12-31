import socket
import sys

data = str.encode(sys.argv[1])
if not sys.argv[1]:
    data = str.encode('hello')

ipaddr = "127.0.0.1"
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバーを指定
    s.connect((ipaddr, port))
    # サーバーにメッセージを送る
    s.send(data)
    # ネットワークのバッファサイズは1024
    # サーバーからの文字列を取得する
    data = s.recv(1024)
    
    print(data)