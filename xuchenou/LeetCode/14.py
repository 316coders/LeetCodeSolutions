"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #空直接返回无
        if not strs:
            return ""        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            #第一个条件是如果有字符串到尾了, 第二个条件是有字符串在i的位置上字母不一样了
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        return strs[0]
s = ["flower","flow","flight"]
c = Solution()
print(c.longestCommonPrefix(s))