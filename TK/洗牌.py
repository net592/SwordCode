import random

def shuffle(l):
    res = []
    for i in range(len(l)):
        idx = random.randrange(i, len(l))
        l[i], l[idx] = l[idx], l[i]
    return list(set(l))

if __name__ == "__main__":
    l=[1,2,3,4,5,5]
    print(shuffle(l))