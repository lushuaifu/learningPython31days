import  multiprocessing

if __name__ == '__main__':
    print('start......')
    #创建一个队列，有三个位置
    q = multiprocessing.Queue(3)
    q.put('a')
    #print(q.qsize())
    q.put('b')
    #q.put('c')
    #q.put('d')                                 #阻塞
    q.put('d',timeout=2)                 #阻塞2秒钟，2秒中之后，如果还没有空闲空间，报错
    #q.put_nowait('d')
    print(q.get())
    print(q.get())
    #print(q.get())
    #print(q.get())           #阻塞
    print(q.get_nowait())
    print('over......')

    #如果不指定参数，无穷尽
    q = multiprocessing.Queue()
    q.put('a')
    q.put('b')
    q.put('c')
    q.put('d')
    q.put('e')
    q.put('f')
    q.put('g')
    q.put([1,2,3])
    print(q.qsize())