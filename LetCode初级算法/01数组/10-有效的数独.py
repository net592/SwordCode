class Solution:
    def isValidSudoku(self, board):
        # 定义rows, cols, boxs 字典
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxs = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                else:
                    #行位置统计
                    rows[i][num] = rows[i].get(num, 0) + 1
                    #列位置统计
                    cols[j][num] = cols[j].get(num, 0) + 1
                    #9个3*3 box
                    boxs_index = (i//3)*3 + j //3
                    boxs[boxs_index][num] = boxs[boxs_index].get(num, 0) + 1
                    print(i, j, num, rows, cols, boxs)
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxs[boxs_index][num] > 1:
                        return False
        return True

if __name__ == '__main__':
    box = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    s=Solution()
    print(s.isValidSudoku(box))