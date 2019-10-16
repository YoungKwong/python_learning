import multiprocessing as mp  #载入multiprocessing模块
import time

def job(v, num, l):  #需要把Lock传进去
    l.acquire()  #.acquirt()锁住
    for i in range(10):
        time.sleep(0.1)
        v.value += num  #想摄取到共享值需要用.value,而不能用=
        print(v.value)
    l.release()  #.release()释放


def multicore():
    l = mp.Lock()  #定义一个Lock锁，避免进程互相争夺共享值
    v = mp.Value('i', 0)  #.Value()定义一个共享值
    p1 = mp.Process(target=job, args=(v, 1, l))  #需要把Lock传进去
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':  #开始运用时，一定要在'__main__'这个框架下，不然会报错
    multicore()

