#只读模式打开一个文件，如果不存在，报错
#f = open('/home/yong/tt.txt','r')
f = open('test.txt','r')
print(f)
#将所有内容读取，打印
print(f.read())
#关闭，释放内存
f.close()
