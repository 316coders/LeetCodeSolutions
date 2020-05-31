"""
target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000

步骤思考
不用考虑了，题目给定一定相等  0.5 检查数组长度，长度不等肯定不行


1.首先需要检查数组是不是同样数字数量相同，如果相同，则可以，不同直接不行。
2.翻转子数组如果只有两个，则相当于是可以对数组中的所有元素进行左右交换。
    2.5假设数组长度为 n，如果数组的位置0已经相等，则动态规划，接下来只需要翻转

"""
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count_numbers = dict()
        for i in target:
            if i in count_numbers:
                count_numbers[i] += 1
            else:
                count_numbers[i] = 1
        for j in arr:
            if j in count_numbers:
                count_numbers[j] -= 1
            else:
                return False
        return True

target = [7,1]
arr = [7,2]
s1 = Solution()
print(s1.canBeEqual(target,arr))