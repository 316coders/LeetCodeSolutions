"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l_result = list()
        length = len(intervals)
        intervals.sort(key = lambda x:x[0]) #根据左区间排序，之后就只用看右区间了
        #有以下3种情况
        # [1,3]  [4,8]    a[1]<b[0]不用合并
        # [1,3]  [2,6]    a[1]>b[0]  and a[1]<b[1] 合并成[a[0],b[1]]
        # [1,5]  [2,4]    a[1]>b[0] and a[1]>=b[1] 删掉b,保留a
        for i in intervals:
            #a[1]<b[0]不用合并
            if not l_result or l_result[-1][1] < i[0]:
                l_result.append(i)
            #如果 a[1]<b[1],尾巴就是b[1],不然就是b在a之内,尾巴还是a[1]
            else:
                l_result[-1][1] = max(l_result[-1][1],i[1])
        return l_result

 
