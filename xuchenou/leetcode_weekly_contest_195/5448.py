"""
5448. 判断路径是否相交
给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。

机器人从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。

如果路径在任何位置上出现相交的情况，也就是走到之前已经走过的位置，请返回 True ；否则，返回 False 。
1 <= path.length <= 10^4
path 仅由 {'N', 'S', 'E', 'W} 中的字符组成
"""
from typing import Dict

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        d1 = dict()
        temp = str(x)+"."+str(y)
        d1[temp] = 1
        for i in path:
            if i == 'N':
                y += 1
            if i == 'W':
                x -= 1
            if i == 'S':
                y -= 1
            if i == 'E':
                x += 1
            temp = str(x)+"."+str(y)
            if d1. __contains__(temp):
                return True
            else:
                d1[temp] = 1
        return False

path = "NESWW"
s1 =  Solution()
print(s1.isPathCrossing(path))
        