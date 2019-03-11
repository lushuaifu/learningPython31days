import socket

# 创建符合ipv4的udp协议实现的socket对象
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(mySocket)


