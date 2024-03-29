class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            print(tmp)
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                  res += tmp[0]
            else:
                break
        return res
      
      
class Solution:
    def longestCommonPrefix(self, s) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s): #遍历每个 列表字符串
            print("i", i, s[i], res)
            while s[i].find(res) != 0: # 判断发现的res, s[i] == res 跳出
                res = res[0:len(res)-1] # 递减继续查找
                print(s, i, s[i], res)
            i += 1
        return res

strs = ["flower", "flow", "flight"]     
s = Solution()
print(s.longestCommonPrefix(strs))
