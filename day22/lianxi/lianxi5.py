import socket as s

# 创建套接字
udpsocket = s.socket(s.AF_INET, s.SOCK_DGRAM)
# 绑定本地相关信息
bindAddr = ('', 6781)
udpsocket.bind(bindAddr)
num = 1
while True:
    # 等待接收对方发送数据
    recvdata = udpsocket.recvfrom(1024)
    # 将接收到的数据再发送给对方
    udpsocket.sendto(recvdata[0], recvdata[1])
    #udpsocket.sendto(str(len(recvdata[0].decode('gbk'))).encode('gbk'), recvdata[1])
    # 统计信息
    print('已经将接收到的%d个数据返回给对方，内容为：%s' % (num, recvdata[0].decode('gbk')))
    num += 1
    # 关闭套接字
udpsocket.close()
