def gen(k):
    i = 1
    print(i)
    while True:
        yield i ** k
        i += 1
    print(i)
        
gen1 = gen(1)
print(gen1)
gen3 = gen(3)
print(gen3)

def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        print(f"循环{i}")
        next_1  = next(gen1)
        next_3 = next(gen3)
        print(f"next_1={next_1}，{sum_1}, next_3={next_3}， {sum_3}")
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1,  sum_3)
    
get_sum(10)
