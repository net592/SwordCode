# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 思路：一般我们删除1个链表节点，直接将其上1个节点的next指向下一个节点就可以了。
        node.val = node.next.val
        node.next = node.next.next