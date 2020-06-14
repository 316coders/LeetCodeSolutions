"""
5423. 找两个和为目标值且不重叠的子数组

给你一个整数数组 arr 和一个整数值 target 。

请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。

请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。
示例 1：

输入：arr = [3,2,2,4,3], target = 3
输出：2
解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
示例 2：

输入：arr = [7,3,4,7], target = 7
输出：2
解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
示例 3：

输入：arr = [4,3,2,6,2,3,4], target = 6
输出：-1
解释：我们只有一个和为 6 的子数组。
示例 4：

输入：arr = [5,5,4,4,5], target = 3
输出：-1
解释：我们无法找到和为 3 的子数组。
示例 5：

输入：arr = [3,1,1,1,5,1,2,1], target = 3
输出：3
解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8
"""
from typing import List
from typing import Set
from collections import defaultdict
#在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 
#请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。
#注意不能重叠,
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        #[3,2,2,4,3]
        length = len(arr)
        res = []
        #第一步: 创建一个新的p = list(),p(i)就是从0-i的和,所以p(i)-p(j)就是从j到i的和.
        p = [0] * (length + 1 )
        for i in range(0,length):
            p[i+1] = p[i] + arr[i]
        #print(p)
        #第二步: 去寻找子数组target,得记录第一个子数组找到的区间,第二个子数组必须在此之后.
        #now_index = 0
        i = -1
        while (i < length +1):
            i += 1
        #for i in range(now_index,length+1):
            #if p[i] == target:
                #temp = [i]
                #res.append(temp)
            for j in range(i+1,length+1):
                interval = p[j] - p[i]  #i+1 到 j 的和
                #已经超过了就没必要继续循环
                if interval > target:
                    i = j+1
                    break
                #如果第一遍找到了,直接跳出循环j,去找下一个,记得注意可能会有n个子数组.
                if interval == target:
                    #尾端考量
                    if i+1 != j:
                        temp = [i+1,j]
                        res.append(temp)
                        i = j+1
                        break            
                    else:
                        res.append([j])
                        i = j+1
                        break 
                    #temp = [i+1,j]
                    #res.append(temp)
                    #i = j+1
                    #break 

        #如果没有返回两个数组,就返回-1

        if(len(res)<2):
            return -1
        else:
            return res


s1 = Solution()
arr = [3,2,2,4,3]
target = 3
print(s1.minSumOfLengths(arr,target))  
#[3, 5, 7, 11, 14]
# [0] [4]

arr2 = [7,3,4,7]
target2 = 7
print(s1.minSumOfLengths(arr2,target2)) 
# [7, 10, 14, 21]
# [0] [1,2] [3]

arr3 = [4,3,2,6,2,3,4]
target3 = 6
print(s1.minSumOfLengths(arr3,target3)) 
#[4, 7, 9, 15, 17, 20, 24]
#-1

arr4 = [5,5,4,4,5]
target4 = 3
print(s1.minSumOfLengths(arr4,target4)) 

arr5 = [3,1,1,1,5,1,2,1]
target5 = 3
print(s1.minSumOfLengths(arr5,target5)) 
#[3, 4, 5, 6, 11, 12, 14, 15]
#[[0], [1, 3], [5, 6]]

arr6 =[1,2,1]
traget6 = 3
print(s1.minSumOfLengths(arr6,traget6)) 
#[1, 3, 4]
