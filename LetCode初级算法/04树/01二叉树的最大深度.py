"""
给定1个二叉树，找出器最大深度
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明：叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，
3
/ \
9 20
/ \
15 7
返回它的最大深度 3 。
思路1：深度优先搜索DFS，递归求解：注意设置终止条件。计算每个节点所在的层数。其中根结点的深度为1，即整棵二叉树的深度=根结点的深度+max(左子树的深度, 右子树的深度)。且每个节点的深度计算公式都是1+max（其左子树的深度，其右子树的深度）
思路2：广度优先搜索BFS，利用队列求解。
按照层次去遍历，依次遍历根节点，然后是左孩子和右孩子，所以要遍历完当前节点的所有孩子。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 解法1 DFS深度查找递归解法
        # 判断跳出条件
        # if not root:
        #     return 0
        
        # 左右递归
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)
        # return max(left, right) + 1 # 当前节点高度是左右子树最高的那颗树高度+1

        # 解法2 BFS 广度搜索解法
        # 跳出条件
        if not root:
            return 0
        
        # 定义栈
        stack = [(1, root)]
        # 定义初始深度
        depth = 0

        while stack:
            # 弹出节点
            cur_depth, node = stack.pop()
            # 如果弹出的节点不为空
            if node:
                depth = max(cur_depth, depth)
                # cur_depth+1 深度递增， 遍历左右孩子
                stack.append((cur_depth+1, node.left)) # 
                stack.append((cur_depth+1, node.right)) 
        return depth