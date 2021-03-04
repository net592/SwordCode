import threading, time


def run1():
    print("grab the 1 part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num


def run2():
    print("grab the 2 part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)


if __name__ == '__main__':

    num, num2 = 0, 0
    lock = threading.RLock()
    for i in range(5):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    print("运行线程数量：",threading.active_count())
else:
    print('----all threads done---',threading.active_count())
    print(num, num2)