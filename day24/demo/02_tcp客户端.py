import socket
import time

# socket对象
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('1......')

'''
连接服务器,
    如果连接上，继续运行
    连接不上，报错
'''
clientSocket.connect(('192.168.11.74',7788))

print('2......')

#关闭
clientSocket.close()