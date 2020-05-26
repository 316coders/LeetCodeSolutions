#题目描述
#众所周知，牛妹非常喜欢吃蛋糕。
#第一天牛妹吃掉蛋糕总数三分之一（向下取整）多一个，第二天又将剩下的蛋糕吃掉三分之一（向下取整）多一个，以后每天吃掉前一天剩下的三分之一（向下取整）多一个，到第n天准备吃的时候只剩下一个蛋糕。
#牛妹想知道第一天开始吃的时候蛋糕一共有多少呢？
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
