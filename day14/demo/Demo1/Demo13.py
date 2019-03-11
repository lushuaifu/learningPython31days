'''
解码：看不懂的字节--->看得懂的字符
编码：看得懂的字符-->看不懂的字节

编码格式：
    linux:utf-8
    windows:gbk
'''
def test1():
    f = open('测试.txt','w',encoding='utf-8')
    f.write('中')
    f.close()

def test2():
    f = open('测试.txt','r',encoding='utf-8')
    ret = f.read()
    print(ret)
    f.close()

def test3():
    f = open('测试.txt','rb')
    ret = f.read()
    print(ret)
    ret = ret.decode('utf-8')
    print(ret)
    f.close()

def test4():
    f = open('测试.txt','rb')
    ret = f.read()
    print(ret)
    f.close()

test1()
test2()
#test3()