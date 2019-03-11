import socket as s
import random

while 1:
    udpsocket = s.socket(s.AF_INET, s.SOCK_DGRAM)
    localAdress=('',random.randint(1024,8888))
    udpsocket.bind(localAdress)
    destAdress = ('192.168.11.79',6789 )
    sendata = input('请输入要发送的数据')
    udpsocket.sendto(sendata.encode('gbk'), destAdress )
    recvdata = udpsocket.recvfrom(1024)
    recvdata = '【Receive from %s : %s】：%s' % (recvdata[1][0], recvdata[1][1], recvdata[0].decode('gbk'))
    print(recvdata)
    udpsocket.close()
    print('over...')
