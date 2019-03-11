import socket as s
#创建套接字
udpsocket = s.socket(s.AF_INET, s.SOCK_DGRAM)
#准备接收方地址
sendAddr = ('192.168.11.79', 6789)
#从键盘获取信息
sendata = input('请输入要发送的数据')
#发送数据到指定电脑
udpsocket.sendto(sendata.encode('gbk'), sendAddr)
#等待接收方发送数据
recvdata = udpsocket.recvfrom(1024)
recvdata = '【Receive from %s : %s】：%s' % (recvdata[1][0], recvdata[1][1], recvdata[0].decode('gbk'))
#显示对方发送数据
print(recvdata)
#关闭套接字
udpsocket.close()
print('over...')
