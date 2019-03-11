import socket
import time

# 买个手机
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 插卡
serverSocket.bind(('', 7788))
# 由飞行模式到接听模式
serverSocket.listen(10)

print('1......')

'''
    newSocket:  服务员
        这个对象可以与当时连接的客户端就行发，收消息
    clientAddr：连接的客户端的信息(ip,port)
'''
# 等待电话打入
newSocket, clientAddr = serverSocket.accept()
print('2......')
print(newSocket)
print(clientAddr)

# time.sleep(100)
# 关
newSocket.close()  # 关闭之后，客户端也会被关闭

serverSocket.close()  # 项目运行中服务器一直运行，不会关闭
