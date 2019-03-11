import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self,name):
        super().__init__(name = name)
    def run(self):
        print('run......')


if __name__ == '__main__':
    p1 = MyProcess('懂不懂')
    p1.start()
    print(p1.name)
