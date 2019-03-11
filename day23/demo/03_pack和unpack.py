import struct

data = struct.pack('!H8sb5sb',1,b'girl.jpg',0,b'octet',0)
print(type(data))
ret1 = struct.unpack('!H',data[:2])
print(ret1[0])

ret1 = struct.unpack('!8s',data[2:10])
print(ret1)
print(ret1[0].decode('utf-8'))

ret1 = struct.unpack('!H8sb5sb',data)
print(ret1)