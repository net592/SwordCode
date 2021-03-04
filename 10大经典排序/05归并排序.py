

arr = [5,1,11,3,-1]
# 迭代法
def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2) # len(arr)>>1
    left, right = arr[0:middle], arr[middle:]
    print(middle, len(arr), arr, left, right)
    return merge(mergeSort(left), mergeSort(right))


def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    print("merge", result, left, right)
    return result


def mergeSort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr) >> 1
    left, rigth = arr[0:mid], arr[mid:]
    return merge(mergeSort(left), mergeSort(rigth))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

if __name__ == '__main__':
    print(mergeSort(arr))