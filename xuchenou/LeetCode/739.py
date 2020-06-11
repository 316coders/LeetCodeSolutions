"""
739. 每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
                    你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #用栈来解决,对于一个新遇到的元素,如果比栈顶小,就入栈,不然栈顶出站,然后其入栈.
        #count = 1
        t_stack = list()
        res = [0] * len(T)
        for i in range(0,len(T)):
            #如果为空直接添加一个
            now_temperature = T[i]
            if not t_stack:
                t_stack.append(i)  #添加下标而不是值,方便记录过了几天
            #当前栈不为空,则用当前输入,与栈顶开始的每一个元素比较,直到栈里面剩余的元素较大
            else:
                while(t_stack and now_temperature > T[t_stack[-1]]):
                    index = t_stack.pop()
                    res[index] = i - index
                #最后添加当前日的气温到栈   
                t_stack.append(i)
        return res
        
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
s1 = Solution()
print(s1.dailyTemperatures(temperatures)) 
                

        