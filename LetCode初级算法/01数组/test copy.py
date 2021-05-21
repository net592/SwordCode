import random
def cusrandom(m):
    n = len(m)
    li = []
    while len(li) < n:
        idx = random.randint(0, n - 1)
        print(m[idx])
        if m[idx] not in li and m[idx] not li:
            li.append(m[idx])
            
            
    return li

m = [1,2,3,3,5]
print(cusrandom(m))