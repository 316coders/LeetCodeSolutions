"""
顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #注意行列可以为0
        rows = len(matrix)
        if rows != 0:
            column = len(matrix[0])
        else:
            column = 0
        print(rows)
        print(column)
        #开始跑路,loop = 圈数 
        loop = 0 
        while():
            #1.从左-->右,列数相关
            #2.从上-->下,行数相关
            #3.从右-->左
            #4.从下-->上
            pass

        return 0

matrix = [[1,2,3,4],[5,6,7,8]]
matrix2 = [[]]  #1行，0列
matrix3 = []  # matrix[0]  list index out of range
s1 = Solution()
print(s1.spiralOrder(matrix))