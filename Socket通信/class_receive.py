import socket

class Receive:
    def __init__(self, clientsock,client_address):
        print(client_address[0]+"が接続しました。")
        self.clientsock = clientsock
        self.client_address = client_address

    def receveMsg(self):
        while True:
            rcvmsg = self.clientsock.recv(1024)
            if rcvmsg.decode() == "disconnect":
                self.delConnect()
                break
            print(self.client_address[0]+": "+rcvmsg.decode())

    def delConnect(self):
        print(self.client_address[0]+"が切断しました。")
        self.clientsock.close()

def receive(host,port):
    serversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    serversock.bind((host,port))
    serversock.listen(10)

    try:
        while True:
            clientsock, client_address = serversock.accept()
            Receive(clientsock,client_address).receveMsg()
    except KeyboardInterrupt: # Ctrl+C でサーバを閉じる
        serversock.close()
        print("\nServer close!!")

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 1270
    receive(host,port)