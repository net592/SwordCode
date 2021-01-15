
# 1 2 3 
# 4 5 6
# 7 8 9
class Solution1:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        #先取矩阵的第一行，接着将剩下作为新矩阵进行一个逆时针90度的翻转，接着获取第一行，直到矩阵为空。
        #需要注意的点pop() 越界，翻转矩阵的时候相当于将列数据变成行数据，可以一列一列获取最后注意顺序。
        if  matrix is None:
            return None
        new_matrix = []
        number = len(matrix) * len(matrix[0])
        new_matrix.extend(matrix[0])
        while len(new_matrix) < number:
            matrix.pop(0)#上边界即为数组的第一个子数组
            matrix = self.turn(matrix)
            new_matrix.extend(matrix[0])
        return new_matrix
    def turn(self, matrix1):
        if  matrix1 is None:
            return None
        turned_lst = [([0] * len(matrix1)) for i in range(len(matrix1[0]))]
        #左边界即为数组从尾到头的每一项子数组的第一个元素
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                turned_lst[j][i] = matrix1[i][len(matrix1[0]) - 1 - j]
        return turned_lst

class Solution2:
  def printMatrix(self, matrix):
    # 打印矩阵
    result = []
    while matrix:
      result += matrix.pop(0)
      if matrix:
        matrix = self.rotate(matrix)
    return result
 
  def rotate(self, matrix):
    # 逆时针旋转矩阵
    row = len(matrix)
    col = len(matrix[0])
    # 存放旋转后的矩阵
    new_matrix = []
    # 行列调换
    for i in range(col):
      new_line = []
      for j in range(row):
        new_line.append(matrix[j][col-1-i])
      new_matrix.append(new_line)
    return new_matrix

if __name__ == "__main__":        
    matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    solution = Solution2()
    result =  solution.printMatrix(matrix)
    print(result)


