# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 使用列表 + 双指针方式求解
    def isPalindrome(self, head: ListNode) -> bool:
        # 解法1 列表反转判断
        arr = [] # 临时空间存储整个链表

        # 循环遍历，把vla存储arr
        while head:
            arr.append(head.val)
            head = head.next

        # 解法2 使用双指针 
        # left, right  = 0, len(arr) -1
        # while left < right:
        #     if arr[left] != arr[right]:
        #         return False
        #     else:
        #         left += 1
        #         right -= 1
        # return True
        
        return arr == arr[::-1] # 方法2 使用Python 列表切片反转特性