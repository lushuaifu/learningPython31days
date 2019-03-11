import socket
import time

'''
serverSocket是用来接收新的客户端的
以后与这个连接的客户端的收发消息就不能用serverSocket了，
而是用返回来的新的newSocket


'''

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('serverSocket:%s'%type(serverSocket))

serverSocket.bind(('', 7788))
serverSocket.listen(10)

newSocket, clientAddr = serverSocket.accept()

print('newSocket:%s'%type(newSocket))

#发
sendData = input('>>')
newSocket.send(sendData.encode('gbk'))
#收
'''
    此时的recv会导致阻塞。
    一旦对应客户端断开了，不阻塞，并返回''的字符串
'''
recvData = newSocket.recv(1024)
#print(recvData.decode('gbk'))
print(recvData)



newSocket.close()
serverSocket.close()
