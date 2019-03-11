import socket as s

#创建套接字
udpsocket=s.socket(s.AF_INET,s.SOCK_DGRAM)
#准备接收方地址
sendAddr=('192.168.11.79',6789)
#从键盘获取数据
sendata=input('请输入要发送的数据')
#发送数据到指定电脑
udpsocket.sendto(sendata.encode('gbk'),sendAddr)
udpsocket.close()