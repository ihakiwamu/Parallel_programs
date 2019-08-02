import socket
import base64
import time
import threading

def display_mode(client):
    while True:
        rcvmsg = client.recv(1024)
        print(rcvmsg.decode())

def setFile(client):
    filename = input("送信ファイル名->")
    client.send(filename.encode())
    with open(filename,'rb') as f:
        client.sendfile(f,0)

def send(host,port):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    print("Successful access to server!")

    try:
        while True:
            msg = input("メッセージ->")
            client.send(msg.encode())
            if msg == "disconnect": break
            elif msg == "file": # ファイルをレシーバに送信する
                setFile(client)
                time.sleep(0.1)
                client.send("end".encode())
            elif msg == "display": # ディスプレイモードに移行する
                display_mode(client)
    except KeyboardInterrupt:
        client.close()
        print("\nDisconnect!!")

if __name__ == "__main__":
    # host = input("Server address->")
    host = "127.0.0.1"
    port = 1270
    send(host,port)