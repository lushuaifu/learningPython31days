import  multiprocessing

if __name__ == '__main__':
    q = multiprocessing.Queue(3)
    q.put('a')
    q.put('b')
    q.put('c')
    #q.put('d',block=False)
    q.put_nowait('d')
