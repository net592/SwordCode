"""给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

1234
4321
"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        暴力破解，数字转字符串，处理范围
        """
        # 将x先转成绝对值正数，之后转成字符串，再切片反转
        s = str(abs(x))[::-1]
        # 处理范围
        if int(s) > 2**31-1 or int(s) < 2**31*-1:
            return 0
        # 处理负数情况
        return int(s) if x > 0 else int(s)*-1

class Solution2:
    def reverse(self, x: int) -> int:
        """[数学方法， %10取余数，然后不断//10 ]

        Args:
            x (int): [description]

        Returns:
            int: [description]
        """

if __name__ == "__main__":
    s = Solution()
    print("run")
    print(s.reverse(1563847412))