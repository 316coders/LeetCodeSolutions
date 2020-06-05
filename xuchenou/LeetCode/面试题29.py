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
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #注意行列可以为0
        maxrows = len(matrix)
        if rows != 0:
            maxcolumn = len(matrix[0])
        else:
            maxcolumn = 0
        print(maxrows)
        print(maxcolumn)
        #开始跑路,当前行列 = 0
        row = 0
        column = 0 
        result = list() 
        while(row <= maxrows and column <= maxcolumn):
            #1.从左-->右,列数相关
            for i in range(0+column,maxcolumn):
                result.append(matrix[column][i])
            row += 1
            #2.从上-->下,行数相关
            for j in range(0+row,maxrows):
                result.append(matrix[j][maxrows])
            column += 1   
            #3.从右-->左
            for k in reversed.range()
            #4.从下-->上
            pass

        return 0
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

matrix = [[1,2,3,4],[5,6,7,8]]
matrix2 = [[]]  #1行，0列
matrix3 = []  # matrix[0]  list index out of range
s1 = Solution()
print(s1.spiralOrder(matrix))