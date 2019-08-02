import socket
import base64
import threading

def receive(host,port):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    client.send("display".encode())
    try:
        while True:
            rcvmsg = client.recv(1024)
            print(rcvmsg.decode())
    except KeyboardInterrupt: # Ctrl+C で閉じる
        client.close()
        print("\nDisconnect!!")

if __name__ == "__main__":
    host = input("Server address->")
    port = 1270
    receive(host,port)