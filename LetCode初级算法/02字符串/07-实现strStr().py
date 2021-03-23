class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 解题思路，通过比较字符串 长度内字符
        L, n = len(haystack), len(needle) # 2个字符串长度
        for start in range(L-n +1): # +1防止溢出
            if haystack[start:start+n] == needle:
                return start
        return -1