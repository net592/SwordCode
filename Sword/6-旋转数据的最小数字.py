"""
https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tags=&title=&diffculty=0&judgeStatus=0&rp=1
Q:把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

思路分析：
使用二分查找
一般的比较原则有：

如果有目标值target，那么直接让arr[mid] 和 target 比较即可。
如果没有目标值，一般可以考虑 端点
情况1，arr[mid] > target：4 5 6 1 2 3
arr[mid] 为 6， target为右端点 3， arr[mid] > target, 说明[first ... mid] 都是 >= target 的，因为原始数组是非递减，所以可以确定答案为 [mid+1...last]区间,所以 first = mid + 1
情况2，arr[mid] < target:5 6 1 2 3 4
arr[mid] 为 1， target为右端点 4， arr[mid] < target, 说明答案肯定不在[mid+1...last]，但是arr[mid] 有可能是答案,所以答案在[first, mid]区间，所以last = mid;
情况3，arr[mid] == target:
如果是 1 0 1 1 1， arr[mid] = target = 1, 显然答案在左边
如果是 1 1 1 0 1, arr[mid] = target = 1, 显然答案在右边
所以这种情况，不能确定答案在左边还是右边，那么就让last = last - 1;慢慢缩少区间，同时也不会错过答案。

INPUT
[3,4,5,1,2]


"""

# -*- coding:utf-8 -*-
class Solution:
    # 寻找断崖点
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 循环所有，比较 当前数 大于 后一个数
        for i in range(len(rotateArray)):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]


class Solution:
    # 暴力循环
    def minNumberInRotateArray(self, rotateArray):
        minimun = rotateArray[0]
        for item in rotateArray:
            if item < minimun:
                minimun = item
        return minimun


if __name__ == '__main__':
    input = [1, 1, 1,0, 1]
    s = Solution()
    print(s.minNumberInRotateArray(input))