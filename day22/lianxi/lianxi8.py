import socket,sys


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
dest=('<broadcast>',6789)
s.sendto('hi'.encode('gbk'),dest)
print('等待对方回复（按ctrl+c退出）')
while 1:
    (buf,address)=s.recvfrom(2048)
    print("Received from %s: %s" % (address, buf.decode('gbk')))