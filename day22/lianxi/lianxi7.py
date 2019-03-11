from socket import *
from time import ctime

udpsocket=socket(AF_INET,SOCK_DGRAM)
bindAddr=('',7788)
udpsocket.bind(bindAddr)
while 1:
    recvdata=udpsocket.recvfrom(1024)
    print('【%s】%s:%s'%(ctime(),recvdata[1][0],recvdata[0]))

udpsocket.close()