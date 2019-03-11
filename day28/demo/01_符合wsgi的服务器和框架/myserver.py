'这是自定义的服务器模块'

import socket
import multiprocessing
import os
import time
import re
import sys


class MyHttpServer(object):
    def __init__(self,application):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSocket = serverSocket
        self.application = application

    def bind(self, port=8000):
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
            #请求信息，字符串
            recvData = clientSocket.recv(1024).decode('gbk')
            '''
            1、按照换行符分割
            2、遍历列表，得到每一行，再按照:分割，第一行除外
        GET / HTTP/1.1
        Host: www.baidu.com
        Connection: keep-alive
        Cache-Control: max-age=0
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
        Accept-Encoding: gzip, deflate, sdch, br
        Accept-Language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4
        Cookie: BDUSS=1kdjlKQlVUUEg1dXV6T0tYRThtUjkxdjZ4cHJCT25rWVE3WmJSbUYydDZPZ3haSVFBQUFBJCQAAAAAAAAAAAEAAACnOEY-5ue6vV9ob21lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHqt5Fh6reRYdG; BAIDUID=5B48A8CD73B157BC742ABD9CC11550F6:FG=1; BIDUPSID=E8E963BF4D88F0EC3F3317C92CE6F01C; PSTM=1497844768; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=0; H_PS_PSSID=1434_21123_17001_20927; BD_UPN=12314353
           '''
            fileName = re.split(r' +', recvData.splitlines()[0])[1]
            method = re.split(r' +', recvData.splitlines()[0])[0]
            env = {
                'PATH_INFO': fileName,
                'METHOD':method
            }
            for item in recvData:
                if item.count(':')!=0:
                    k,v = item.split(':')
                    env[k] = v
            responseBody = self.application(env,self.startResponse)

            sendData = (self.responseHeader + os.linesep + os.linesep + responseBody).encode('gbk')
            clientSocket.send(sendData)
            clientSocket.close()

    def startResponse(self, status, responseHeaders):
        self.responseHeader = status+os.linesep
        for k, v in responseHeaders:
            kv = (k + ':' + v + os.linesep)
            self.responseHeader += kv

def main():
    print(sys.argv)
    moduleName, attrName = sys.argv[1].split(':')
    myModule = __import__(moduleName)
    server = MyHttpServer(getattr(myModule,attrName))
    server.bind(8000)
    server.start()

if __name__ == '__main__':
    main()
