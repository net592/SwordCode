class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # 字符串转列表，对比排序后，值大小
      s = list(s)
      t = list(t)
      s.sort()
      t.sort()
      s == "".join(s)
      t == "".join(t)
      if s == t:
        return True
      else:
        return False
      # 列表循环删除法
      # return collections.Counter(s) == collections.Counter(t)
      """
      用哈希表统计第一个字符串中的字符数量；
      再统计第二个字符串时，若字符在哈希表中，计数减一，否则返回false
      最后判断哈希表中值是否都为0
      """
       if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True

if __name__ =="__main__":
  s=Solution()
  print(s.isAnagram("abc", "bac"))
