"""
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
示例：
输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k
"""
from typing import List

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        #将List A 先转换成 P[i] = sum(A[0] …… A[i])
        P = list()
        count = 0
        for i in A:
            count += i
            P.append(count)
        print(P)

        #根据同余定理：(P[j]-P[i-1] )mod K == same，计算模K表
        K_dict = {0:1}
        for i in P:
            mod =  i % K
            if mod not in K_dict:
                K_dict[mod] = 1
            else:
                K_dict[mod] += 1
        print(K_dict)

        #对相同mod余的排列组合得到总计
        solutions = 0
        for i in K_dict:
            j = K_dict[i]
            solutions = (j * (j-1) / 2) + solutions
        return int(solutions)

#A = [4,5,0,-2,-3,1]
#K = 5
A = [5]
K = 9
S = Solution()
print(S.subarraysDivByK(A,K))