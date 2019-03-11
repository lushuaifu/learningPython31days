import socket
import multiprocessing
import os
import time
import re

G_PATH = './html'

def serverHandler(clientSocket, clientAddr):
    '与请求的客户端进行交互'
    # 接收客户端发来的消息
    recvData = clientSocket.recv(1024).decode('gbk')
    # 获取请求头(字符串的第一行)
    a = recvData.splitlines()[0]
    b = re.split(r' +', a)
    fileName = b[1]
    '''
    如果是/       默认读取index.html
    如果能找到    读
    如果找不到    设置404
    '''
    filePath = G_PATH
    if '/'==fileName:
        filePath+='/index.html'
    else:
        filePath += fileName

    #异常处理读取文件
    try:
        #模拟异常
        num = 1/0

        file  = None
        file = open(filePath,'r',encoding='gbk')
        responseBody = file.read()

        responseLine = 'HTTP/1.1 200 OK' + os.linesep
        responseHeader = 'Server: laowang' + os.linesep
        responseHeader += 'Date: %s' % time.ctime() + os.linesep
    except FileNotFoundError:
        responseLine = 'HTTP/1.1 404 NOT FOUND' + os.linesep
        responseHeader = 'Server: laowang' + os.linesep
        responseHeader += 'Date: %s' % time.ctime() + os.linesep
        responseBody = '找不到'
    except Exception:
        responseLine = 'HTTP/1.1 500 ERROR' + os.linesep
        responseHeader = 'Server: laowang' + os.linesep
        responseHeader += 'Date: %s' % time.ctime() + os.linesep

        responseBody = '服务器正在升级中，请稍后再试。。。。。。'
    finally:
        if (file!=None) and  (not file.closed):
            file.close()

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
