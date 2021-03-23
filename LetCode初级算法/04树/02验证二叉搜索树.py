# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # node > node.left and node < node.right
        # 使用DFS 深度递归解法
        def dfs(node, min_val, max_val):
            if not node:
                return True

            # 判断 根值 与 上下区间值比较
            if not min_val < node.val < max_val:
                return False
            
            # 递归深度判断 左右 2棵树
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
        # 传root, 最小，最大边界值
        return dfs(root, -2**32, 2**32) # 判断上下区间