class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i],爬到这里的时候有n种方法
        #dp[1] = 1 ,dp[2] = 2,dp[3] = dp[2] + dp[1] 
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return (int)(fibn / sqrt5)