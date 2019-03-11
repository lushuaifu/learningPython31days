'''
    应用程序可以在通用的tcp/ip协议基础上，加上自己的判断，组成新的应用层协议。
    比如飞秋，使用的是udp协议，在此基础上包装成了IPMSG协议。
    格式：
    版本号:包编号:发送者姓名:发送者机器名:命令字:消息
    1:12323434:user:machine:32:hello


    注：现行的IPMSG协议的版本是1
'''
import socket

#创建socket对象
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#目的地
destAdress = ('192.168.11.74',2425)
#消息内容
sendMsg = input('>>')
#编码
sendMsg = sendMsg.encode('gbk')
#发送
udpSocket.sendto(sendMsg,destAdress)

#关闭socket对象
udpSocket.close()
print('over......')