import  hashlib

m = hashlib.md5()
m.update('1234565'.encode('utf-8'))
s = m.hexdigest()
print(s)
