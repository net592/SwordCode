"""
给定1个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现1次，返回移除后数组的新长度。
不需要使用额外的数组空间，你必须在原地修改输入数组并在使用O（1）额外空间的条件下完成。
说明：为什么返回数值是整数，但输出的答案是数组呢
注意：输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下：
//nums是以“引用”方式传播的，也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);
思路：只不过这道题的难度在于，在操作中不能随意改变数组中原本元素的位置，因为你要保持它后面的数字还是有序的，才好去比较相邻的数字是否一样。
因此，我们弄1个变量记录上1个单独的数字，再弄1个变量记录该数字后面的位置序号，往后遍历，直到遇到不一样的数字，才把那个数字放到该位置序号上来，然后把记录单独数字的变量设为这个新数字，记录位置的变量序号+1，继续往后遍历，因为是随着遍历过程往前放数字，所以不会影响到后面的数字顺序。
Def removeDuplicates(nums):
If len(nums)<=1:
Return len(nums)
Slow = 0
If i range(1, len(nums)):
If nums[i]!=nums[slow]:
Slow += 1
Nums[slow] = nums[i]
Return slow+1
"""

class Solution:
    def removeDuplicates(self, nums: int) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        思路：
        定义一个慢指針，保存前一个位置，
        循环比较，下一个i值与慢指针值，如果不相等，则向后滑动，
        循环完成，返回slow +1（补上前一位）
        我们弄1个变量slow记录上1个单独的数字，再弄1个变量记录该数字后面的位置序号，往后遍历，直到遇到不一样的数字，
        才把那个数字放到该位置序号上来，然后把记录单独数字的变量设为这个新数字，记录位置的变量序号+1，
        继续往后遍历，因为是随着遍历过程往前放数字，所以不会影响到后面的数字顺序。
        """
        if len(nums) <=1:
            return len(nums)
        # 定义一个慢指标
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]: #其中nums[slow]表示上1个数字
                slow += 1 # 计数器+1
                print(nums,slow, nums[slow], nums[i])
                nums[slow] = nums[i] # 
            else:
                print("dup", nums[i], slow)
        slow += 1
        return slow

if __name__ == '__main__':
    nums = [5,5,3,10,1]  # [5,3,10,1] 4
    s = Solution()
    print(s.removeDuplicates(nums))