# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #迭代
        new_head = None
        while head:
            p = head # 构建p
            head = head.next # 缩短链表，减去前面已经遍历的
            p.next = new_head # 将下一节点的next指向自己
            new_head = p
        return new_head