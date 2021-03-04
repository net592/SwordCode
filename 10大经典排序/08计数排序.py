"""
计数排序（Counting Sort）
计数排序须知：
计数排序要求输入数据的范围在 [0,N-1] 之间，则可以开辟一个大小为 N 的数组空间，将输入的数据值转化为键存储在该数组空间中，数组中的元素为该元素出现的个数。它是一种线性时间复杂度的排序。
计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
计数排序(Counting sort)是一种稳定的排序算法。计数排序使用一个额外的数组C，其中第i个元素是待排序数组A中值等于i的元素的个数。然后根据数组C来将A中的元素排到正确的位置。它只能对整数进行排序。

算法描述
找出待排序的数组中最大和最小的元素；
统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。
"""

def countingSort(nums):
    bucket = [0] * (max(nums) + 1) # 桶的个数
    for num in nums:  # 将元素值作为键值存储在桶中，记录其出现的次数
        bucket[num] += 1
        print(bucket, bucket[num], num)
    print(bucket)
    i = 0  # nums 的索引
    for j in range(len(bucket)):
        print(j)
        while bucket[j] > 0: #表示存在该值
            print("j", bucket, nums, i, nums[i], j)
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums


if __name__ == '__main__':
    nums = [4,6,5,9,1,1]
    print(countingSort(nums))