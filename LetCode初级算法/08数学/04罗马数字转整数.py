class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}  # 字典  
        total= 0 # 总数
        # 遍历字符 查询结果
        for i in range(len(s)):
            # 如果i<len(s)-1 表示在左侧，s[i] < s[i+1] 说明左侧小于右侧 即为 特殊情况 要建
            # "IX" 9  10-1
            if i<len(s)-1 and roman[s[i]] < roman[s[i+1]]: 
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total