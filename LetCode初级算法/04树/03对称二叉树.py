# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 采用DFS递归查找，判断左右2棵树的值
        def dfs(root1, root2):
            if root1 == root2: return True # 对称
            if not root1 and root2: return False # 非对称
            if root1 and not root2: return False # 非对称
            if root1.val != root2.val: return False # 非对称
            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        # 跳出条件
        if not root: return True
        return dfs(root.left, root.right)