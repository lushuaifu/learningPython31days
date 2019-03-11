import socket
'''
1、一对一  点对点          单播
2、一对多                  多播
3、一对所有                广播
'''
#创建socket对象
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#开启广播
udpSocket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
#目的地：如果是''表示当前IP，如果是'<broadcast>'表示当前所在的广播地址
destAdress = ('<broadcast>',2425)
#消息内容
sendMsg = input('>>')
#编码
sendMsg = sendMsg.encode('gbk')
#发送
udpSocket.sendto(sendMsg,destAdress)

while True:
    (content,address) = udpSocket.recvfrom(1024)
    print("received from %s----%s" % (address, content.decode('gbk')))

#关闭socket对象
udpSocket.close()
print('over......')