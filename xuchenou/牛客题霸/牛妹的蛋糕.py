#
# 
# @param n int整型 只剩下一只蛋糕的时候是在第n天发生的．
# @return int整型
#
class Solution:
    def cakeNumber(self , n ):
        cake = 1
        for i in range(1,n):
            cake = cake + 1
            cake = int (cake * 3  / 2 )
        return cake
