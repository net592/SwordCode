# _*_ coding=utf-8 _*_


"""
实现一个二叉树结果，并进行遍历
             E
           /  \
          A    G
           \    \
            C    F
           / \
          B   D
"""
from collections import deque


class BinaryTree(object):
    def __init__(self, data):
        self.data = data
        self.child_l = None
        self.child_r = None


# 创建
a = BinaryTree("A")
b = BinaryTree("B")
c = BinaryTree("C")
d = BinaryTree("D")
e = BinaryTree("E")
f = BinaryTree("F")
g = BinaryTree("G")

# 构造节点关系
e.child_l = a
e.child_r = g
a.child_r = c
c.child_l = b
c.child_r = d
g.child_r = f

# 设置根
root = e


def pre_order(tree):
    """
    前序遍历:root -> child_l -> child_r
    :param tree: the root of tree
    :return:
    """
    if tree:
        print(tree.data, end=',')
        # print("")
        pre_order(tree.child_l)
        pre_order(tree.child_r)


def in_order(tree):
    """
    中序遍历：child_l -> root -> child_r
    :param tree:
    :return:
    """
    if tree:
        in_order(tree.child_l)
        print(tree.data, end=',')
        in_order(tree.child_r)


def post_order(tree):
    """
    后序遍历：child_l -> child_r -> root
    :param tree:
    :return:
    """
    if tree:
        post_order(tree.child_l)
        post_order(tree.child_r)
        print(tree.data, end=',')


def level_order(tree):
    """
    层次遍历：E -> AG -> CF -> BD
    使用队列实现
    :param tree:
    :return:
    """
    queue = deque()
    queue.append(tree)          # 先把根添加到队列
    while len(queue):           # 队列不为空
        node = queue.popleft()
        print(node.data, end=',')
        if node.child_l:
            queue.append(node.child_l)
        if node.child_r:
            queue.append(node.child_r)


pre_order(root)
print('')
in_order(root)
print('')
post_order(root)
print('')
level_order(root)