import socket
'''
    udp协议的socket发送消息
'''
#创建socket对象
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#确定对象目的地ip和端口号port，组成一个元组
destAdress = ('192.168.11.74',7788)
#发送内容到目标机器上，内容要编码
msg = input('>>')
msg = msg.encode('gbk')
udpSocket.sendto(msg,destAdress)
#udpSocket.sendto('abc'.encode('utf-8'),destAdress)
#udpSocket.sendto(b'abc',destAdress)
#关闭socket对象
udpSocket.close()