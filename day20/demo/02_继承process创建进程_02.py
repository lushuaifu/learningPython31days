import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self):
        super().__init__()
    def run(self):
        print('run......')


if __name__ == '__main__':
    p1 = MyProcess()
    p1.start()
