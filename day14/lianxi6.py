import time
try:
    f=open('test.txt')
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    except:
        pass
    finally:
        f.close()
        print('关闭文件')
except:
    print('没有这个文件')
