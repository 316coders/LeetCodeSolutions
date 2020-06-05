"""
238. 除自身以外数组的乘积
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

输入: [1,2,3,4]
输出: [24,12,8,6]

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #两个数组 left_mul 和 right_mul ，记录对应位置的左乘与右乘.
        #left_mul[5] = 0*1*2*3*4   ,left[0] = 1

        #cal left_mul
        left_mul = [0] * len(nums)
        left_mul[0] = 1
        for i in range(1,len(nums)):
            left_mul[i] = nums[i-1] * left_mul[i-1]
        
        #cal right_mul
        right_mul = [0] * len(nums)
        right_mul[len(nums)-1] = 1
        #for i in range(len(nums),-1,-1):
        for i in reversed(range(len(nums) - 1)):
            right_mul[i] = nums[i+1] * right_mul[i+1]

        #cal pes
        product_except_self = [0] * len(nums)
        for i in range(len(nums)):
            product_except_self[i] = left_mul[i] * right_mul[i]
        return product_except_self

l1 = [1,2,3,4]
s1 = Solution()
print(s1.productExceptSelf(l1))
