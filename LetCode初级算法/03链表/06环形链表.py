# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 采用快慢指针解法
        # 判断head 是否存在
        if not head or not head.next:
            return False

        # 声明快慢指针
        slow, fast = head, head.next

        # 跳出循环条件，slwo==fast 及 slow和fast交集，意味有环路
        while slow != fast: 
            # 如果没有fast，跳出
            if not fast or not fast.next:
                return False
            # slow乌龟 slow兔子
            slow = slow.next
            fast = fast.next.next # 兔子比乌龟快一步  
        return True
        # '''
        # 思路2：快慢指针法
        # '''
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow==fast:
        #         return True#当快慢指针相遇，则说明有环
        # return False