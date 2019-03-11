from multiprocessing import Pool
import os,time,random

'''
    进程池里的任务需要自己start()?                  不需要
    进程池里的任务，是按照放入的顺序的执行的吗？      不是
    哪个进程执行哪个任务，咱能手动干预吗？            不能

    1、第一步：设置进程池中进程的数量
            进程池的数字根据硬件环境进行设定，一般设置为cpu的数量
    2、第二步：放任务
    3、第三步：关闭进程池  close
    4、第四步：开始干活，  join
            进程池中的进程开始执行任务
            如果任务大于进程的数量，多余的任务等待
            一旦某个进程完成当下的任务，从等待的任务中随机找一个任务执行。

'''

def worker(msg):
    time.sleep(random.random() * 2)
    #time.sleep(random.random()*2)
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    #random.random()随机生成0~1之间的浮点数
    #time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))
if __name__ == '__main__':
    po=Pool(4) #定义一个进程池，最大进程数3
    for i in range(0,10):
        #Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
        #每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker,(i,))

    print("----start----")
    #po.apply_async(worker, (111,))
    po.close() #关闭进程池，关闭后po不再接收新的请求
    #po.terminate()
    po.join()  #等待po中所有子进程执行完成，必须放在close语句之后
    print("-----end-----")
