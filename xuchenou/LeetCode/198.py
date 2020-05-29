"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""
from typing import List

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        best_money = 0
        #如果选择偷n，那么最高金额等于 n + rob(n-2)
        #如果不偷n，则最高金额等于 rob(n-1)
        if(len(nums)> 2):
            best_money = max(nums[-1] + self.rob(nums[:-2]),self.rob(nums[:-1]))
            return best_money
        elif(len(nums) == 2):
            return max(nums[0],nums[1])
        elif(len(nums) == 1):
            return nums[0]
        else:
            return 0
"""           
class Solution:
    def rob(self, nums: List[int]) -> int:
        #防止输入空数组
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[size - 1]
dp = [0] * 4
print(dp)

test = [1,2,3]
print(test[:-2])

S = Solution()
print(S.rob(test)) 


