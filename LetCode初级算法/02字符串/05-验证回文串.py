class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 第一种 直接切割反转字符串
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]
        
        # 第二种解法 过滤符号空格
        sgood = "".join([i.lower() for i in s if i.isalnum()])
        left, right = 0, len(sgood) -1
        while left < right:
            if sgood[left] == sgood[right]:
                left +=1
                right -=1
            else:
                return False
        return True

if __name__ == "__main__":
    s=Solution()
    print(s.isPalindrome("aabaa"))