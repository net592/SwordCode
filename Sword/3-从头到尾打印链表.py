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

https://zhuanlan.zhihu.com/p/22923273
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        print(self.val, self.next)


class Solutions:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        arrayList = []
        while listNode:
            arrayList.append(listNode.val)
            listNode = listNode.next
        return arrayList[::-1]


if __name__ == '__main__':
    l = ListNode({67,0,24,58})
    s = Solutions()
    print(s.printListFromTailToHead(l))