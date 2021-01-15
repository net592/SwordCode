"""
Q:请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

"""


class Soultions:
    # s 源字符串
    def replaceSpace(self, s):
        """
        使用原生的replace方法，暴力
        :param s:
        :return:
        """
        # write code here
        tmp = s.replace(" ", "%20")
        return tmp


class Solution:
    """
    遍历替换法
    """
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        str=''
        for i in s:
            if i==' ':
               i = '%20'
            str=str+i
        return str

if __name__ == '__main__':
    s = Soultions()
    print(s.replaceSpace("We Are Happy"))