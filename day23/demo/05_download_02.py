import socket
import struct
import os
import time

def main():
    #创建文件
    myFile = open('xx.avi','wb')
    #socket对象，发送下载的请求信息，接收信息和发送确认信息
    udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #服务器地址
    destAddr = ('192.168.11.74',69)
    #pack信息
    data = struct.pack('!H7sb5sb', 1, b'110.avi', 0, b'octet', 0)
    #发送
    udpSocket.sendto(data,destAddr)
    #定义一个变量，记录写的次数
    num = 0
    #循环
    while True:
        #接收
        recvData,redvAddr = udpSocket.recvfrom(1024)

        #unpack信息，获取操作码
        operNum = struct.unpack('!H',recvData[:2])[0]
        #判断
        if operNum==3:
                # unpack信息，获取块编号
                blockNum = struct.unpack('!H', recvData[2:4])[0]
                print(blockNum)

                #判断
                num = num+1
                if num==65536:
                    num = 0

                if num == blockNum:
                    num = blockNum
                    #获取数据，写到文件中
                    myFile.write(recvData[4:])
                    #准备ack数据
                    ackData = struct.pack('!HH', 4,blockNum)
                    #发送ack确认到服务器
                    udpSocket.sendto(ackData,redvAddr)

            if len(recvData)<516:
                break

        if operNum==5:
            print('发生异常啦......')
            break
    #关闭文件
    myFile.close()

if __name__ == '__main__':
    main()