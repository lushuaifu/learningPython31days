'''
    参数的传递：
        1、传递数字、字符串、None，修改后。不影响原来的
        2、其它的都是影响原来的
'''

def f1(a):
    a.append(10)

def f2(a):
    a+=1

if __name__ == '__main__':
    num = [1,2,3]
    f1(num)
    print(num)

    num = 1
    f2(num)
    print(num)
