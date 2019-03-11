import multiprocessing

if __name__ == '__main__':
    m = multiprocessing.Manager()
    print(m)
    q = m.Queue()
    print(q)

    q = multiprocessing.Queue()
    print(q)