import socket

#创建socket对象
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
'''
绑定,
第一个参数是本地ip，不指定也可以，默认会帮你填充,建议不写
第二个参数是端口号，不要与本地的端口号冲突
'''
localAdress = ('',8081)
udpSocket.bind(localAdress)
#目的地
destAdress = ('192.168.11.74',8080)
#消息内容
#sendMsg = input('>>')
#编码
#sendMsg = sendMsg.encode('gb2312')
#发送
#udpSocket.sendto(sendMsg,destAdress)

'''
收,这个缓冲区不是越大越好，如果发送方的数据，大于缓冲区，丢包，报错。
如果收不到，阻塞
'''
print('收消息等待中.....')
recvMsg = udpSocket.recvfrom(1024)
recvMsg = '【Receive from %s : %s】：%s'%(recvMsg[1][0],recvMsg[1][1],recvMsg[0].decode('gbk'))
print(recvMsg)

#关闭socket对象
udpSocket.close()
print('收到消息，over......')