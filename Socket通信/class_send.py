import socket

def send(host,port):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    print("Successful access to server!")
    while True:
        msg = input("メッセージ->")
        client.send(msg.encode())
        if msg == "disconnect": break
    client.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 1270
    send(host,port)
