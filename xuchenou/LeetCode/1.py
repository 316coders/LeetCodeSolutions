"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = list()
        for i in nums:
            if((target - i ) in nums):
                if(nums.count(i) == 2):
                    #print("true")
                    result.append(nums.index(i))
                    result.append(nums[nums.index(i)+1:].index(i)+nums.index(i)+1)
                    return result
                    #print(nums[nums.index(i)+1:].index(i))
                elif(i != target - i):
                    result.append(nums.index(i))
                    result.append((nums.index(target-i)))
                    return result
        return result
nums = [3,3]
target = 6
s1 = Solution()
print(s1.twoSum(nums,target))