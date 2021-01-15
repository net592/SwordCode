import time
import datetime

def calculate_function_run_time(func):
    """
    Calculate the running time of the function
    :param func: the function need to been calculated
    :return:
    """
    def call_fun(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        end_time = time.time()
        print('%s() run time：%s s' % (func.__name__, int(end_time - start_time)))
        return f
    return call_fun

def calculate_function_run_time_ms(func):
    def call_fun(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        end_time = time.time()
        print('%s() run time：%s ms' % (func.__name__, int(1000*(end_time - start_time))))
        return f
    return call_fun


@calculate_function_run_time
def test1():
    for i in range(1000000):
        i = i +1

@calculate_function_run_time_ms
def test2():
    for i in range(1000000):
        i = i +1

if __name__ == "__main__":
    test1()
    test2()

