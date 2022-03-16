"""
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
"""
class A(object):
    def __init__(self):
        self.foo = 2
        
    bar = 1

    def func1(self, cc,*args, **kwarg):
        print('foo', cc, args, kwarg)

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        print(cls.__init__)
        cls().func1()  # 调用 foo 方法
a = A()
a.func1("a", a=1, b=2)
# a.func2()
# ###########
# A.func2()  # 不需要实例化