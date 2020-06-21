"""
验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """str.isalunm
        Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise. A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
        """
        #filter creates a list of elements for which a function returns true
        #两个函数结合,过滤出了所有的字母
        temp = filter(str.isalnum,s)
        temp2 = "".join(temp).lower()
        return temp2 == temp2[::-1]

str1 = "A man, a plan, a canal: Panama"
s = Solution()
print(s.isPalindrome(str1))