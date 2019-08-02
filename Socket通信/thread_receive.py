import socket
import base64
import time
import threading
import os

# 複数接続のコードを参照したサイト
# https://torina.top/detail/253/

# グローバルなので気をつけてくださいいいいいい
clients = []
smsg = ""

# ユーザごとのフォルダを作成する
def creatDir(address):
    if not os.path.exists("./user/"+address):
        os.mkdir("./user/"+address)
    return "./user/"+address+"/"

def splitName(filename):
    name = filename.split("/")
    return name[len(name)-1]

# 受信したファイルの復元
def copy(file,filename,dir):
    with open(dir+filename,'ab') as f:
        f.write(file)

# ファイルを受診する。
def getFile(clientsock,client_address):
    print(client_address[0]+"からファイルを受信します。")
    filename = clientsock.recv(1024)
    filename = splitName(filename.decode())
    dir = creatDir(client_address[0])
    while True:
        file = clientsock.recv(1073741824)
        if file == "end".encode(): break
        copy(file,filename,dir)
    print(client_address[0]+"より、"+filename+"を受信しました。")

# displayにメッセージを送信する。
def shareMsg(clientsock,client_address):
    global smsg
    print(client_address[0]+"はディスプレイモードに移行します。")
    while True:
        if smsg:
            clientsock.send(smsg.encode())
            smsg = ""

# クライアントとの接続を切る
def remove_conection(clientsock, client_address):
    print(client_address[0]+"が切断しました。")
    clientsock.close()
    clients.remove((clientsock, client_address))

# クライアントからのメッセージの受信
def handler(clientsock, client_address):
    global smsg
    smsg = client_address[0]+"が接続しました。"
    while True:
        rcvmsg = clientsock.recv(1024)
        if rcvmsg.decode() == "disconnect":
            smsg = client_address[0]+"が切断しました。"
            remove_conection(clientsock,client_address)
            break
        if rcvmsg.decode() == "file":
            getFile(clientsock,client_address)
            continue
        if rcvmsg.decode() == "display":
            shareMsg(clientsock,client_address)
        print(client_address[0]+": "+rcvmsg.decode())
        smsg = client_address[0]+": "+rcvmsg.decode()

def receive(host,port):
    wait_start = time.time()
    serversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    serversock.bind((host,port))
    serversock.listen(2)

    try:
        while True:
            clientsock, client_address = serversock.accept()
            print(client_address[0]+"が接続しました。")
            clients.append((clientsock, client_address))
            handle_thread = threading.Thread(target=handler,args=(clientsock, client_address),daemon=True)
            handle_thread.start()
    except KeyboardInterrupt: # Ctrl+C でサーバを閉じる
        serversock.close()
        print("\nServer close!!")

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 1270
    receive(host,port)