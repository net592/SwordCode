"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

input
7,[
    [1,2,8,9],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]
    ]
output
true

#1 
两种思路
一种是：
把每一行看成有序递增的数组，
利用二分查找，
通过遍历每一行得到答案，
时间复杂度是nlogn

#2 另外一种思路是：
利用二维数组由上到下，由左到右递增的规律，
那么选取右上角或者左下角的元素a[row][col]与target进行比较，
当target小于元素a[row][col]时，那么target必定在元素a所在行的左边,
即col--；
当target大于元素a[row][col]时，那么target必定在元素a所在列的下边,
即row++；
/* 思路
* 矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，
* 因此从左下角开始查找，当要查找数字比左下角数字大时。右移
* 要查找数字比左下角数字小时，上移
*/
"""


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表 合并数组 判断偷懒
    def Find(self, target, array):
        # write code here
        rows = len(array)
        tmp_array = []
        for i in range(rows):
            tmp_array += array.pop(0)
            print(tmp_array)
        if target in tmp_array:
            print(True)
            return True
        else:
            return False


class Solution:
    """
    利用二维数组由上到下，由左到右递增的规律，
    那么选取右上角或者左下角的元素a[row][col]与target进行比较，
    当target小于元素a[row][col]时，那么target必定在元素a所在行的左边,
    即col--；
    当target大于元素a[row][col]时，那么target必定在元素a所在列的下边,
    即row++；
    """
    def Find(self, target, array):
        """
        查询
        :param target: 比较值
        :param array: 二维数组
        :return:  True False
        """
        rows = len(array) - 1 
        cols = len(array[0]) - 1
        row = rows
        col = 0
        print(col <= cols, row >= 0)
        # 判断如果超出界限，认为没有找到包含
        while col <= cols and row >= 0:
            # 判断目标值 小于 元素，如果真，所在行向↑偏移查询
            if target < array[row][col]:
                print(row, col, "==", target, array[row][col],)
                # 向上查询 行号 -1
                row -= 1
            # 判断目标值 大于 元素，如果真，所在列→偏移查询
            elif target > array[row][col]:
                print(row, col, "==", target, array[row][col],)
                # 列+1 查询
                col += 1
            # 不大于，不小于，就是等于，及找到相等值，True
            else:
                return True
        # 没有找到，出界
        return False


if __name__ == "__main__":
    input_1 = 4
    input_2 = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    s = Solution()
    print(s.Find(input_1, input_2))