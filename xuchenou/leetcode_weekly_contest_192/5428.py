"""
5428. 重新排列数组
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

"""
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = list()
        for i in range(0,n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res

nums = [2,5,1,3,4,7]
n = 3 
s1 = Solution()
print(s1.shuffle(nums,n))
