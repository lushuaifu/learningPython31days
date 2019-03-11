'这是自定义的服务器模块'

import socket
import multiprocessing
import os
import time
import re


class MyHttpServer(object):
    '描述服务器，显示的页面'

    def __init__(self):
        '''
            初始化，
            这里初始化了一个socket对象，作为实例变量
            这里初始化了一个HTMLPATH，作为静态页面所在的文件夹
        '''
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSocket = serverSocket
        self.HTMLPATH = './html'

    def bind(self, port=8000):
        '''
        绑定端口号
        port:要绑定的端口号
        '''
        self.serverSocket.bind(('', port))

    def start(self):
        self.serverSocket.listen()
        while True:
            # 接收
            clientSocket, clientAddr = self.serverSocket.accept()
            print(clientSocket)
            # 开一个新的进程，执行交互
            multiprocessing.Process(target=self.clientHandler, args=(clientSocket, clientAddr)).start()
            # 关闭客户端对象
            clientSocket.close()

    def clientHandler(self, clientSocket, clientAddr):
        try:
            recvData = clientSocket.recv(1024).decode('gbk')
            fileName = re.split(r' +', recvData.splitlines()[0])[1]

            filePath = self.HTMLPATH

            if fileName.endswith('.py'):  # 动态资源
                try:
                    pyname = fileName[1:-3]
                    # 导入
                    pyModule = __import__(pyname)

                    env = {}
                    responseBody = pyModule.application(env, self.startResponse)

                    responseLine = self.responseLine
                    responseHeader = self.responseHeader
                except ImportError:
                    responseLine = 'HTTP/1.1 404 NOT FOUND'
                    responseHeader = 'Server: laowang' + os.linesep
                    responseHeader += 'Date: %s' % time.ctime()
                    responseBody = '<h1>找不到<h1>'




            else:  # 静态资源
                if '/' == fileName:
                    filePath += '/index.html'
                else:
                    filePath += fileName

                try:
                    file = None
                    file = open(filePath, 'r', encoding='gbk')
                    responseBody = file.read()

                    responseLine = 'HTTP/1.1 200 OK'
                    responseHeader = 'Server: laowang' + os.linesep
                    responseHeader += 'Date: %s' % time.ctime()
                except FileNotFoundError:
                    responseLine = 'HTTP/1.1 404 NOT FOUND'
                    responseHeader = 'Server: laowang' + os.linesep
                    responseHeader += 'Date: %s' % time.ctime()
                    responseBody = '<h1>找不到<h1>'
                finally:
                    if (file != None) and (not file.closed):
                        file.close()
        except Exception as ex:
            responseLine = 'HTTP/1.1 500 ERROR'
            responseHeader = 'Server: laowang' + os.linesep
            responseHeader += 'Date: %s' % time.ctime()
            responseBody = '服务器正在升级中，请稍后再试。。。。。。'
            print(ex)
        finally:
            sendData = responseLine + os.linesep + responseHeader + os.linesep + os.linesep + responseBody
            print(sendData)
            sendData = sendData.encode('gbk')
            clientSocket.send(sendData)
            if (clientSocket != None) and (not clientSocket._closed):
                clientSocket.close()

    def startResponse(self, status, responseHeaders):
        '''
        整合responseHeader
        :param status:              状态码
        :param responseHeaders:     响应头[('Server','laowang'),('Date','Tue Jun 20 14:32:26 2017')]
        :return:
        '''
        self.responseLine = status
        self.responseHeader = ''
        for k, v in responseHeaders:
            kv = (k + ':' + v + os.linesep)
            self.responseHeader += kv


if __name__ == '__main__':
    server = MyHttpServer()
    server.bind(8000)
    server.start()
