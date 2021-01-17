"""
Q:输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
输入{67,0,24,58}
返回值[58,24,0,67]
解释:ListNode 链表
ListNode
刷LeetCode碰到一个简单链表题，题目已经定义了链表节点ListNode，作者很菜，好多忘了，把ListNode又查了一下

struct ListNode {
       int val;    //定义val变量值，存储节点值
       struct ListNode *next;   //定义next指针，指向下一个节点，维持节点连接
  }
在节点ListNode定义中，定义为节点为结构变量。
节点存储了两个变量：value 和 next。value 是这个节点的值，next 是指向下一节点的指针，当 next 为空指针时，这个节点是链表的最后一个节点。
注意注意val只代表当前指针的值，比如p->val表示p指针的指向的值；而p->next表示链表下一个节点，也是一个指针。
构造函数包含两个参数 _value 和 _next ，分别用来给节点赋值和指定下一节点
参考：
链表的定义：
链表(linked list)是由一组被称为结点的数据元素组成的数据结构，每个结点都包含结点本身的信息和指向下一个结点的地址。
由于每个结点都包含了可以链接起来的地址信息，所以用一个变量就能够访问整个结点序列。也就是说，结点包含两部分信息：
一部分用于存储数据元素的值，称为信息域；另一部分用于存储下一个数据元素地址的指针，称为指针域。
链表中的第一个结点的地址存储在一个单独的结点中，称为头结点或首结点。链表中的最后一个结点没有后继元素，其指针域为空。　　
https://www.jb51.net/article/76915.htm
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        print(self.val, self.next)


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        arrayList = []
        # 循環插入列表，然後最後取反
        while listNode:
            arrayList.append(listNode.val)
            print(arrayList, listNode.val)
            # next 下一個
            listNode = listNode.next
        return arrayList[::-1]


class Solution:
    # 使用循環遞歸
    def printListFromTailToHead(self, listNode):
        # 使用插入0 來實現倒序插入
        arrayList = []
        while listNode:
            print(arrayList, listNode.val)
            arrayList.insert(0, listNode.val)
            # next 下一個
            listNode = listNode.next
        return arrayList


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # 方法一  使用栈, 先進後出
        if not listNode:
            return []
        temp = []
        result = []
        while listNode:
            temp.append(listNode.val)  # 进栈
            listNode = listNode.next
        while temp:
            result.append(temp.pop())  # 出栈
        return result

        # 方法二  使用递归
        result = []

        def solutions(Node):
            if Node:
                solutions(Node.next)  # 先递归到最后一层
                result.append(Node.val) # 添加值，退出函数，返回到上一层函数中的这行，继续添加值

        solutions(listNode)
        return result

        # 方法三 使用从头到尾遍历，逆序输出
        result = []
        while listNode:
            result.append(listNode.val)
            listNode = listNode.next
        return result[::-1]



if __name__ == '__main__':
    # 组装一个单跳表 1-2-3-4
    head = ListNode(1)
    item2 = ListNode(2)
    item3 = ListNode(3)
    item4 = ListNode(4)
    head.next = item2
    item2.next = item3
    item3.next = item4
    # 解法
    s = Solution()
    print(s.printListFromTailToHead(head))
