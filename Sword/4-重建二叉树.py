"""
Q:输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


描述
这道题综合考察了对二叉树的前序，中序遍历算法的理解，和根据数组建立二叉树的代码考察以及对递归代码的理解与运用。
题目难度：二星
考察知识：树，递归

题解
本题解是初学算法的对象，一步步从不会到会的详细讲解。
方法：递归算法
前置知识：
二叉树的前序遍历：根左右
二叉树的中序遍历：左根右
二叉树的的后序遍历：左右根
介绍完了二叉树的定义及基本性质，接下来，我们需要了解二叉树的遍历。所谓二叉树的遍历，指的是如何按某种搜索路径巡防树中的每个结点，使得每个结点均被访问一次，而且仅被访问一次。对于二叉树，常见的遍历方法有：先序遍历，中序遍历，后序遍历，层序遍历。这些遍历方法一般使用递归算法实现。
  先序遍历的操作定义为：若二叉树为空，为空操作；否则（1）访问根节点；（2）先序遍历左子树；（3）先序遍历右子树。
  中序遍历的操作定义为：若二叉树为空，为空操作；否则（1）中序遍历左子树；（2）访问根结点；（3）中序遍历右子树。
  后序遍历的操作定义为：若二叉树为空，为空操作；否则（1）后序遍历左子树；（2）后序遍历右子树；（3）访问根结点。
  层序遍历的操作定义为：若二叉树为空，为空操作；否则从上到下、从左到右按层次进行访问。
链接：https://www.jianshu.com/p/9503238394df
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        """
        # 通过前序 第一个根 ， 查找 左侧 和 右侧， 递归查询
        假如有前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}
        从前序pre知根节点是第一个元素1，从中序知元素1前面的[4,7,2]都是左子树，[5,3,8,6]是右子树
        递归可建得二叉树
        :param pre: 前序排序
        :param tin: 中序排序
        :return: TreeNode
        """
        if not pre or not tin:
            return None
        root_value = pre[0]  # 获取根
        root = TreeNode(root_value)  # 实例
        k = tin.index(root_value) # 查找中序 索引未知
        print(f"root:{pre[0]}, indexf{k}, pre:{pre}, tin:{tin}")
        root.left = self.reConstructBinaryTree(pre[1:k + 1], tin[0: k]) # 查找左侧序列
        root.right = self.reConstructBinaryTree(pre[k+1:], tin[k +1:])  # 查找右侧序列
        return root


if __name__ == '__main__':
    s = Solution()
    result =s.reConstructBinaryTree([1,2,3,4,5,6,7], [3,2,4,1,6,5,7])