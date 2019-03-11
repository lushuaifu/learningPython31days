import socket
import time


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('192.168.11.74',7788))

print('clientSocket:%s'%type(clientSocket))

#发
sendData = input('>>')
clientSocket.send(sendData.encode('gbk'))
#收
recvData = clientSocket.recv(1024)
print(recvData.decode('gbk'))



clientSocket.close()

