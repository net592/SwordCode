# 装饰器写法

def my_dec(func):
    def wrapper(*args, **kwargs):
        print("wrapper",*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@my_dec
def my_fun(*args):
    print("myfun", *args)

my_fun('1',"2")
dir(my_fun())
help(my_fun)
print(my_fun.__name__)
print(my_fun.__name__)

def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat(4)
def greet(message):
    print(message)

#greet('hello world')
