import socket
import time
import threading


def socketState(newSocket,clientAddr):
    print(id(newSocket))

    while True:
        recvData = newSocket.recv(1024)
        recvData = recvData.decode('gbk')
        if recvData == '':
            print('客户端%s退出了...'%clientAddr[0])
            newSocket.close()
            break
        else:
            print('来自于%s:%s的消息(%s):%s'%(clientAddr[0],clientAddr[1],time.strftime('%Y-%m-%d %H:%M:%S'),recvData))
            sendData = 'echo:%s'%recvData
            newSocket.send(sendData.encode('gbk'))


def main():
    #创建服务端socket对象
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', 7788))
    serverSocket.listen(10)
    #循环，等待多个客户端连接
    while True:
        #等待客户端的连接，阻塞。连接后，继续运行
        newSocket, clientAddr = serverSocket.accept()

        print(id(newSocket))

        #创建新的线程，执行与新客户端的交互
        serverThread = threading.Thread(target=socketState, args=(newSocket,clientAddr))
        serverThread.start()
        # 这里不能关闭，多线程共享数据
        #newSocket.close()


if __name__ == '__main__':
    main()