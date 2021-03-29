class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        :return [[7,4,1],[8,5,2],[9,6,3]]
        """
        # 解法思路，转换成 对角线交换，最后反转交换
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                # 黑暗45度交换
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # 每行倒置位置
            matrix[i] = matrix[i][::-1]
        return matrix


if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    s=Solution()
    print(s.rotate(matrix))