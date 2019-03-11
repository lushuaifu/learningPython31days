import socket
import multiprocessing
import os
import time


def serverHandler(clientSocket, clientAddr):
    '与请求的客户端进行交互'
    # 接收客户端发来的消息
    recvData = clientSocket.recv(1024).decode('utf-8')
    print(recvData)
    # 服务端向客户端发消息,作为响应
    responseLine = 'HTTP/1.1 200 OK' + os.linesep
    responseHeader = 'Server: laowang' + os.linesep
    responseHeader += 'Date: %s' % time.ctime() + os.linesep
    responseBody = '老王'
    sendData = (responseLine + responseHeader + os.linesep + responseBody).encode('gbk')

    clientSocket.send(sendData)
    # 关闭
    clientSocket.close()


def main():
    '程序入口'
    # socket对象
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定的端口号，可以重复使用端口号
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定
    serverSocket.bind(('', 8000))
    # 监听
    serverSocket.listen()
    while True:
        # 接收
        clientSocket, clientAddr = serverSocket.accept()
        print(clientSocket)
        # 开一个新的进程，执行交互
        multiprocessing.Process(target=serverHandler, args=(clientSocket, clientAddr)).start()
        # 关闭客户端对象
        clientSocket.close()


if __name__ == '__main__':
    main()
