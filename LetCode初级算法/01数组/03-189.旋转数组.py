


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        最简单的思路：
        直接遍历k,将得到的数字插入list的第1个位置，最后只返回前len(nums)的list即可
        但是！！！注意，本题需要原地修改nums，即不能return任何数组，因此我们这里不能采用上面这种方法
        !!我没考虑到的是：给出的k可能会大于数组长度，这时候就要对原数组取模，才会得到真正需要旋转的个数！
        @但是我们发现编程实现有问题，因此下面的代码，直接根据旋转数组之后的特征，来对
        原数组进行切分，经过3次反转来达到最终目的
        三次翻转，先整体翻转，然后根据K的位置前后局部翻转。
        '''
        print(nums)
        if len(nums)==0 or k==0:
            return
        def reverse(start, end, s):
            while start<end:
                print(start, end)
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            print("s", s)
        n = len(nums)-1
        k = k%len(nums)  # 给出的k可能会大于数组长度，这时候就要对原数组取模
        reverse(0, n, nums)  # 反正所有 [7, 6, 5, 4, 3, 2, 1]
        reverse(0, k-1, nums)  # 反转k前一组 3 [5, 6, 7, 4, 3, 2, 1]
        reverse(k, n, nums)  # 反正k后剩余一组4  [5, 6, 7, 1, 2, 3, 4]
        return nums
if __name__ == '__main__':
    s= Solution()
    print(s.rotate([1,2,3,4,5,6,7], 3))