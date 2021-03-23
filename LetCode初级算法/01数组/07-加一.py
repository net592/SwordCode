class Solution:
    """
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        newstr = ''
        # list -> str
        for i in digits:
            newstr += str(i)
        # str -> int
        newnum = int(newstr)
        newnum += 1
        # int -> str
        newnewstr = str(newnum)
        newlst = []
        # str -> list
        for i in newnewstr:
            newlst.append(int(i))
        return newlst
    
    def plusOne(self, digits: List[int]) -> List[int]:
        # 正常解法 从后往前依次判断末尾是否为9 如果是 则去除：
        newlst = []
        while digits and digits[-1] == 9:
            digits.pop()
            newlst.append(0)
        if not digits:
            return [1] + newlst
        else:
            digits[-1] += 1
            return digits + newlst