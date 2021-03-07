class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        :return [1,3,12,0,0]
        """
        slow = 0
        # 把所有i不等于0的数，向前移动
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[slow] = nums[i]
                slow += 1 # 索引加一
        # 将后面的位置，换成0
        for j in range(slow, len(nums)):
            nums[j] = 0
        return nums

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        :return [1,3,12,0,0]
        """
        j = 0
        # 两个指针i和j
        for i in range(len(nums)):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[i] !=0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums


if __name__ == '__main__':
    s=Solution()
    nums = [0,0,1]
    print(s.moveZeroes(nums))