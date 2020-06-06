"""
128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        num_set = set(nums)

        for num in num_set:
            #例：3开始的长度为 3-n，如果数组里面有2，则2-n的长度一定比3-n长。
            #所以如果一个数，有左边，则只需要考虑左边的那个了。（可以减少运行时间）
            if num - 1 not in num_set:
                current_num = num
                current_length= 1

                #从这个数的右边开始数数
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                #当前数的最长 与 之前记录的最长比较
                longest  = max(longest , current_length)

        return longest 

