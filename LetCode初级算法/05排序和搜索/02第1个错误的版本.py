# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 使用二分法开始解题
        left, right = 1, n # 声明
        while left <= right:
            mid = (left + right) //2
            if isBadVersion(mid):
                right = mid -1
            else:
                left = mid +  1
        return left