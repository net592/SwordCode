class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 声明头和尾，（len(s)-1）尾巴的索引位置
        l,r = 0, len(s)-1
        # 跳出条件l>r
        while l<r:
            # 首尾置换
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        return s
    
        # 第二种解法 s[:]直接数组
        s[:]=s[::-1]
        return s