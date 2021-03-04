import threading
import os
import time
import ctypes

num =100


def test(n):
    global num
    num -= 1
    print("test", num, n)


# 使用函数
def main():
    for i in range(4):
        t1 = threading.Thread(target=test, args=(i,))
        t1.start()  # 启动线程
        print(t1.getName())  # 获取线程名
        print("\nthread parent id:", os.getpid())  # 无法获取线程号，只能获取进程号

# 继承类
class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  # 定义每个线程要运行的函数
        print("running on number:%s" % self.num)
        time.sleep(3)
        test(1)

def main():
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
