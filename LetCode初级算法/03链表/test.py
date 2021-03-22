class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

t1 = TreeNode(val=0, left=1, right=2)
t2 = TreeNode(val=t1, left=4,right=5)\

print(t2.val.val)
