'''
收和发互相不影响：
    这是两个独立的功能，可以考虑两个线程
'''
from socket import *
from threading import *
import  os

'''全局变量'''
# socket
udpSocket = None
# ip
destIp = None
# port
destPort = None


# 收
def recv():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print("\r<<%s:%s%s>>" % (str(recvInfo[1]), recvInfo[0].decode('gbk'),os.linesep),end='')


# 发
def send():
    while True:
        info = input('>>')
        udpSocket.sendto(info.encode('gbk'), (destIp, destPort))


# 主方法
def main():
    global udpSocket
    global destIp
    global destPort

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindAddr = ('', 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    udpSocket.bind(bindAddr)

    #destIp = input("对方的ip:")
    #destPort = int(input("对方的port:"))
    destIp = '192.168.11.74'
    destPort = 8080

    tSend = Thread(target=send)
    tRecv = Thread(target=recv)

    tSend.start()
    tRecv.start()


if __name__ == '__main__':
    main()