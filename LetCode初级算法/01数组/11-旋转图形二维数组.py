class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        :return [[7,4,1],[8,5,2],[9,6,3]]
        """
        m = 0
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                print(i, j, matrix[i][j], matrix[j][i])
                # temp = matrix[i][j]
                # matrix[i][j] = matrix[j][i]
                # matrix[j][i] = temp
                # 交换元素
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
            matrix[i] = matrix[i][::-1]
        return matrix


if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    s=Solution()
    print(s.rotate(matrix))