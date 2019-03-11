import  threading

def process_student(num):
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    std = Student(num)
    do_task_1(std)
    do_task_2(std)


def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)


def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)


if __name__ == '__main__':
    for i in range(1000):
        t = threading.Thread(target=process_student,args=(i,))
        t.start()


'''
    在多线程中，如果使用全局变量，会出问题，一旦一个线程修改了，会影响其它线程。
    如果使用局部变量，一旦想让这个局部变量，一直使用下去，一直传参，比较麻烦。

    既不想使用全局变量，又一直想用这个局部变量。
    可以将这个局部变量绑定到对应的线程中，以后此线程一直用个。
    与其它线程中的无关。
'''