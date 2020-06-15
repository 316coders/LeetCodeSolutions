"""
5437. 不同整数的最少数目
给你一个整数数组 arr 和一个整数 k 。现需要从数组中恰好移除 k 个元素，请找出移除后数组中不同整数的最少数目。

示例 1：
输入：arr = [5,5,4], k = 1
输出：1
解释：移除 1 个 4 ，数组中只剩下 5 一种整数。
示例 2：

输入：arr = [4,3,1,1,3,3,2], k = 3
输出：2
解释：先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。
提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
from typing import List
from typing import Dict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        length = len(arr)
        #思路
        #hash表统计每一个数字出现的次数,比如 5:2 4:1
        d1 = dict()   #{4: 1, 3: 3, 1: 2, 2: 1}
        for i in arr:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        #对dict sort? 按value排序
        d2 = sorted(d1.items(),key = lambda item:item[1])  #[(4, 1), (2, 1), (1, 2), (3, 3)]
        #根据k个删掉对应个 字典对,注意最后一对
        num_type = len(d2)  #4
        for key,value in d2:
            k = k-value
            if k < 0:
                break
            else:
                num_type -= 1
        #最后剩下几个字典,就是返回几种
        return(num_type)



arr = [4,3,1,1,3,3,2]
k = 3
s = Solution()
print(s.findLeastNumOfUniqueInts(arr,k))
#{4: 1, 3: 3, 1: 2, 2: 1}
arr2 = [5,5,4]
k2 = 1
print(s.findLeastNumOfUniqueInts(arr2,k2))
