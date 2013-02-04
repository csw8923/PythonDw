import threading
from time import sleep, ctime
def thread1():
    print 'Thread1 start at:', ctime()
    sleep(4)
    print 'Thread1 done at:', ctime()
def thread2():
    print 'Thread2 start at:', ctime()
    sleep(5)
    print 'Thread2 done at:', ctime()
def main():
    print 'Main start at:', ctime()
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print 'Main done at:',ctime()
if __name__ == '__main__':
    main()