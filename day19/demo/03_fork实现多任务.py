import os
import time


def dance():
        for i in range(3):
                print("正在跳舞...%d"%i)
                time.sleep(1)
def sing():
        for i in range(3):
                print("正在唱歌...%d"%i)
                time.sleep(1)


if __name__ == '__main__':
        pid  = os.fork()

        if pid==0:
                dance()
        else:
                sing()