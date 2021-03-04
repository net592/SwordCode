"""
二位数组旋转90度
"""

def Rotate(data):
    # data = [[i for i in range(4)] for raw in range(4)]
    for ele in data:
        print(ele)
    # 数组长度
    n = len(data)
    for i in range(n):  # 外层循环
        for j in range(i+1, len(data[i])):  # 内层循环 i+1 第一个数不用旋转
            # 交换数据
            print(i, j, data[i][j], data[j][i])
            temp = data[i][j]
            data[i][j] = data[j][i]
            data[j][i] = temp
    return data
data = [[1,2,3], [1,2,3], [1,2,3]]


#2 第二种使用ZIP
def Rotate2(data):
    list_of_tuples = zip(*data[::-1])
    return [list(elem) for elem in list_of_tuples]
    print(data)


print(Rotate(data))
