
array = [2, 20, 5,1,3,10]
def quick_sort(array, left, right):
    if left == right:
        return array
    if left > right:
        return

    low = left
    high = right
    key = array[low]
    while left < right:
        # 找到右边第一个小于于key的数值下标
        while left < right and array[right] > key:
            right -= 1
        # 左拆右补
        array[left] = array[right]
        # 找到左边第一个大于等于于key的数值下标
        while left < right and array[left] <= key:
            left += 1
        # 右拆左补
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1) # 左序列
    quick_sort(array, left + 1, high)  # 右序列
    return array

def quickSort2(array, left, right):  # 这种写法的平均空间复杂度为 O(logn) \
    print(array)
    # 分区操作
    def partition(array, left, right):
        pivot = array[left]  # 基准值
        while left < right:
            while left < right and array[right] >= pivot:
                right -= 1
            print(array, array[left], array[right], pivot)
            array[left] = array[right]  # 比基准小的交换到前面
            while left < right and array[left] <= pivot:
                left += 1
            print(array, array[left], array[right], pivot)
            array[right] = array[left]  # 比基准大交换到后面
        print(array, array[left], array[right], pivot)
        array[left] = pivot # 基准值的正确位置，也可以为 array[right] = pivot
        return left  # 返回基准值的索引，也可以为 return right
    # 递归操作
    if left < right:
        pivotIndex = partition(array, left, right)
        print("index", pivotIndex, left, right)
        l = quickSort2(array, left, pivotIndex - 1)  # 左序列
        r = quickSort2(array, pivotIndex + 1, right) # 右序列
        print("inter", array, l, r)
    return array


def quickSort(array):  # 这种写法的平均空间复杂度为 O(nlogn)
    if len(array) <= 1:
        return array
    pivot = array[0]  # 基准值
    left = [array[i] for i in range(1, len(array)) if array[i] < pivot] 
    right = [array[i] for i in range(1, len(array)) if array[i] >= pivot]
    print(left, [pivot], right)
    return quickSort(left) + [pivot] + quickSort(right)


if __name__ == '__main__':
    #print(quickSort2(array, 0, len(array)-1 ))
    print(quickSort(array))