"""
现有重复数字的有序数组的二分查找
输出在数组中第一个大于等于查找值的位置，如果数组中不存在这样的数，则输出数组长度加一。
输入
5,4,[1,2,4,4,5]
输出
3
"""

#
# 二分查找
# @param n int整型 数组长度
# @param v int整型 查找值
# @param a int整型一维数组 有序数组
# @return int整型
#
class Solution:
    def upper_bound_(self , n , v , a ):
        # write code here
        left = 0
        right = n
        #还有查找空间就继续找,没有就返回n+1
        while left < right:
            mid = (left + right) / 2
            #mid比v大,更新right
            if a[mid] >= v:
                #刚好mid-1的值<v  mid的值>=V,直接返回mid+1
                if mid == 0 or a[mid-1] < v:
                    return mid + 1
                #更新 right = mid
                else:
                    right = mid
            #mid比v小,更新left
            else:
                left = mid + 1
        return n + 1
