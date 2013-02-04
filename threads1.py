import threading,time
class MyThread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)

    def run(self):
        for i in xrange(10):
            print self.getName(),i
            time.sleep(1)

my = MyThread('test')
my.start()