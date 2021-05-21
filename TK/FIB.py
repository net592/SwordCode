# 递归
def fib(n):
    # 0, 1, 1, 2,3,5
    # 从第三个开始，斐波那契数列
    # F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(0))
# 迭代
def fib(n):
    i, num1, num2 = 0, 1, 1
    res = []
    while i < n:
        res.append(num1)
        num1, num2 = num2, num1 + num2
        i += 1
    print(res)
    return res[n-1]

def fib(n):
    a,b,c = 0,0,1
    while a < n:
        print(c) 
        b, c = c, b+c
        a += 1
    return True

print(fib(10))
