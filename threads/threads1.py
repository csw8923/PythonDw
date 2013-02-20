# -*- coding: utf-8 -*-
import threading,time
class MyThread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)

    def run(self):
        for i in xrange(10):
            print self.getName(),i
            time.sleep(1)
#多线程 进程1
my1 = MyThread('test')
my1.start()
#多线程 进程2
my2 = MyThread('test2')
my2.start()