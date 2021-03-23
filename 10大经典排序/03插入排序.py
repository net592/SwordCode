"""
插入排序（Insertion Sort）
插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，
因为只要打过扑克牌的人都应该能够秒懂。插入排序是一种最简单直观的排序算法，
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。

算法描述
一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
从第一个元素开始，该元素可以认为已经被排序；
取出下一个元素，在已经排序的元素序列中从后向前扫描；
如果该元素（已排序）大于新元素，将该元素移到下一位置；
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
将新元素插入到该位置后；
重复步骤2~5。
"""

arr = [10,3,5,11,1]
def insertionSort(arr):
    print(arr)
    for i in range(len(arr)): # 遍历所有索引
        preIndex = i-1 
        current = arr[i]
        print(i , preIndex, current)
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]  # 后移动一位
            preIndex -= 1  # 向前滑动一位
        arr[preIndex+1] = current
    return arr

def insert_sort(arr):
    """
    插入排序：假定左边都是有序的，将右边的数一个一个插入到左边有序数列中
    """
    print(arr)
    # 结算列表的长度
    n = len(arr)
    # 外层循环控制从头走到尾的次数
    for i in range(n):
        preIndex = i - 1
        # 将要比较的数
        current = arr[i]
        # 在左边有序数列总找到所有比当前数更大的数
        while preIndex >= 0 and arr[preIndex] > current:
            # 元素后移
            arr[preIndex + 1] = arr[preIndex]
            # 往前遍历
            preIndex -= 1
        # 找到插入位置后，插入
        print(arr[preIndex + 1], current)
        arr[preIndex + 1] = current
    return arr

def insert_sort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        # 比较后续元素, 大于cureent的向后移动一位
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        # 最前的索引 preIndex + 1 替换值
        print(arr, i, preIndex+1, arr[preIndex + 1], current)
        arr[preIndex + 1] = current
    return arr

if __name__ == '__main__':
    print(insert_sort(arr))

