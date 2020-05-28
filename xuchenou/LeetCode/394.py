""" 394 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""
import re

class Solution:
    def decodeString(self, s: str) -> str:
        pattern=re.compile(r'(\d+)\[(\w+)\]')  #建立正则匹配项
        m = pattern.findall(s)  #从左到右找到所有的项，返回 a list of tuples
        while m:
            for num,char in m:
                s=s.replace(f'{num}[{char}]',int(num) * char)
                print(s)
            m=pattern.findall(s)  #需要考虑[]嵌套的情况
        return s


s = "2[abc]3[cd]ef"
#\d 数字， \d+ 任意个，\w+ 任意个字母   \[ 匹配括号  \]
#pattern=re.compile(r'(\d+)\[(\w+)\]')  #建立正则匹配项
#m = pattern.findall(s)  #从左到右找到所有的项，返回 a list of tuples
#string = ""
#print(m)
#for i in m:
#    print(int(i[0]) * i[1])

sol = Solution()
print(sol.decodeString(s))