'''
只要出现异常，就会找对应的except处理，如果处理不了，或者找不到。程序结束。
'''

def test1():
    print("----test1-1----")
    print(num)
    print("----test1-2----")


def test2():
    print("----test2-1----")
    test1()
    print("----test2-2----")


def test3():
    try:
        print("----test3-1----")
        test1()
        print("----test3-2----")
    except Exception as result:
        print("捕获到了异常，信息是:%s" % result)

    print("----test3-2----")


#test3()
#print("------华丽的分割线-----")
test2()
