"""
给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。

"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1_index = 0
        max2_index = 1
        for i in range(2,len(nums)):
            if nums[i] > nums[max1_index]:
                max1_index = i
        for j in range(2,len(nums)):
            if nums[j] > nums[max2_index] and j != max1_index:
                max2_index = j        
        max = (nums[max1_index] - 1) * (nums[max2_index] - 1)
        return max


nums = [3,7]
s1 = Solution()
print(s1.maxProduct(nums))