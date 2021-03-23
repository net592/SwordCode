class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1): return '1' # 特殊情况处理
        num = self.countAndSay(n-1)+"*"
        temp = list(num)
        count = 1
        strBulider = ''
        print(num, len(temp), temp)
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]:
                count += 1
            else:
                if temp[i] != temp[i+1]:
                    strBulider +=  str(count) + temp[i]
                    count = 1
        return strBulider

class Solution:
    #https://leetcode-cn.com/problems/count-and-say/solution/38-wai-guan-shu-lie-shuang-zhi-zhen-by-yiluolion/
    def countAndSay(self, n: int) -> str:
        pre = ''
        cur = '1'

        # 从第 2 项开始
        for _ in range(1, n):
            # 这里注意要将 cur 赋值给 pre
            # 因为当前项，就是下一项的前一项。有点绕，尝试理解下
            pre = cur
            # 这里 cur 初始化为空，重新拼接
            cur = ''
            # 定义双指针 start，end
            start = 0
            end = 0
            # 开始遍历前一项，开始描述
            while end < len(pre):
                print(start, end, len(pre), cur, pre)
                # 统计重复元素的次数，出现不同元素时，停止
                # 记录出现的次数，
                while end < len(pre) and pre[start] == pre[end]:
                    end += 1
                # 元素出现次数与元素进行拼接
                cur += str(end-start) + pre[start]
                # 这里更新 start，开始记录下一个元素
                start = end
        
        return cur



if __name__ == "__main__":
    s=Solution()
    print(s.countAndSay(3))