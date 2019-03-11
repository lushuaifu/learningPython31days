import time
try:
    f = open('123.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        #如果在读取文件的过程中，产生了异常，那么就会捕获到
        #比如 按下了 ctrl+c
        print('except...')
    finally:
        print('finally...')
        f.close()
        print('关闭文件')
except:
    print("没有这个文件")
