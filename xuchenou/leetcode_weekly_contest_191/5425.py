"""
5425. 切割后面积最大的蛋糕
矩形蛋糕的高度为 h 且宽度为 w，给你两个整数数组 horizontalCuts 和 verticalCuts，其中 horizontalCuts[i] 是从矩形蛋糕顶部到第  i 个水平切口的距离，类似地， verticalCuts[j] 是从矩形蛋糕的左侧到第 j 个竖直切口的距离。

请你按数组 horizontalCuts 和 verticalCuts 中提供的水平和竖直位置切割后，请你找出 面积最大 的那份蛋糕，并返回其 面积 。由于答案可能是一个很大的数字，因此需要将结果对 10^9 + 7 取余后返回。
2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
题目数据保证 horizontalCuts 中的所有元素各不相同
题目数据保证 verticalCuts 中的所有元素各不相同

"""
from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        #将蛋糕边缘加入 h v list中
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.append(0)
        verticalCuts.append(0)
        #刀法排序
        horizontalCuts.sort()
        verticalCuts.sort()        
        #找垂直数组中每两位的间隔
        List1 = list()
        for i in range(0,len(horizontalCuts)-1):
            List1.append(horizontalCuts[i+1] - horizontalCuts[i]) 
        print(List1)

        #找水平数组中每两位的间隔
        List2 = list()
        for j in range(0,len(verticalCuts)-1):
            List2.append(verticalCuts[j+1] - verticalCuts[j]) 
        print(List2)

        m1 = max(List1)
        m2 = max(List2)
        #取余数
        m = 1000000007
        i = 1
        i = (i * m1) % m
        i = (i * m2) % m
        print(i)
        #biggest_cake = m1 * m2
        return i



h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]
s1 = Solution()
s1.maxArea(h,w,horizontalCuts,verticalCuts)

#for i in range(0,2):
#    print(i)