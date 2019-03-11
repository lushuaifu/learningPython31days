import socket as s
#创建套接字
udpsocket = s.socket(s.AF_INET, s.SOCK_DGRAM)
#获取本地ip地址和端口号
localAdress=('',4567)
#绑定本地相关信息
udpsocket.bind(localAdress)
destAdress = ('192.168.11.79', 6789)
sendata = input('请输入要发送的数据')
udpsocket.sendto(sendata.encode('gbk'), destAdress )
#等待对方发送数据，1024表示本次接收的最大字节数
recvdata = udpsocket.recvfrom(1024)
recvdata = '【Receive from %s : %s】：%s' % (recvdata[1][0], recvdata[1][1], recvdata[0].decode('gbk'))
#显示接收到的消息
print(recvdata)
#关闭套接字
udpsocket.close()
print('over...')
