# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 构建递归函数，使用二分索引法，升序构建2棵树
        # TreeNode [中，左，右] 前序
        def bin_build_tree(low, high):
            # low, high 索引位置
            if low > high:
                return None
            # 中位数
            mid = (low + high)//2
            root = TreeNode(nums[mid])
            # low, high
            root.left = bin_build_tree(low, mid-1)
            root.right = bin_build_tree(mid+1, high)
            return root
        return bin_build_tree(0, len(nums)-1)