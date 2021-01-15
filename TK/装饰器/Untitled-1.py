
def primeCnt(n):#埃拉托色尼筛选法，返回小于n的素数
    primes = [True] * (n+1)#范围0到n的列表
    p = 2#这是最小的素数
    while p * p <= n:#一直筛到sqrt(n)就行了
        if primes[p]:#如果没被筛，一定是素数
            for i in range(p * 2, n + 1, p):#筛掉它的倍数即可
                primes[i] = False
        p += 1
    primes = [element for element in range(2, n) if primes[element]]#得到所有少于n的素数
    return primes
print(primeCnt(100))