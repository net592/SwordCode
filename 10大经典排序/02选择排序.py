"""
选择排序

选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

1. 算法步骤

首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置

再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

重复第二步，直到所有元素均排序完毕。
"""

arr = [5, 1, 10, 2, 6]

def selectionSort(arr):
    for i in range(len(arr) - 1):  # 选择排序次数
        # 记录最小数的索引
        minIndex = i
        print(i, minIndex)
        for j in range(i+1, len(arr)): # 索引比较 后续所有元素
            if arr[j] < arr[minIndex]: # 如果发现小的 将索引置为 该位置
                print(arr[j], arr[minIndex])
                minIndex = j
        # 如果 i 不是最小数时，将i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr









def selectionSort(arr):
    for i in range(len(arr)-1):  # 选择排序次数
        minIndex = i
        for j in range(i +1, len(arr)):  # 比较后续元素
            print(i+1, len(arr))
            if arr[j] < arr[minIndex]:
                minIndex = j
        # 如果 i 不是最小数，置换元素
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


if __name__ == '__main__':
    print(selectionSort(arr))