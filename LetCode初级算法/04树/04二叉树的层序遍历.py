# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 定义存储结果，存储每层值
        res = []
        # 定义递归函数
        def helper(tree, depth):
            # 跳出条件
            if not tree: return
            print(len(res), depth, tree.val)
            # 创建当前层列表
            if len(res) == depth:
                res.append([])
            # 追加本层值，到列表
            res[depth].append(tree.val)
            # 递归左右数
            helper(tree.left, depth +1)
            helper(tree.right, depth +1)
        # 传入树和层级
        helper(root, 0)
        return res