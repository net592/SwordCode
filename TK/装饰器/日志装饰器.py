# 定义一个装饰器
def logger(func)
    def wrapper(*args, **kw):
        print("我要开始计算了：{}".format(func.__name__))
        
        # 真正执行的函数
        func(*args, **kw)
        
        print("我结束了")
    return wrapper