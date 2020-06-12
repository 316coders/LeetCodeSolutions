"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

#对于每一个nums中的元素,找剩余元素有无 b+c = -a ,这里n复杂度了
from typing import List
from typing import Set
from collections import defaultdict

#写法超时了
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums) #获取数组长度
        d1 = defaultdict(list)
        res = list()
        #开始建立两两元素之和的hashmap,
        for i in range(0,length):
            for j in range(i,length):
                if(i != j):
                    two_sum = nums[i] + nums[j]
                    d1[two_sum].append([i,j])
        #print(d1)
        #-1: [{0, 1}, {1, 4}], 0: [{0, 2}, {2, 4}], 1: [{0, 3}, {1, 2}, {3, 4}], -2: [{0, 4}, {3, 5}], -5: [{0, 5}, {4, 5}], 2: [{1, 3}], -4: [{1, 5}], 3: [{2, 3}], -3: [{2, 5}]})
        #根据hashmap去查找有无 b+c = -a
        #l_temp = list()
        for k in range(0,length):
            now_value = - nums[k]
            if now_value in d1:
                for l in d1[now_value]:
                    #现在的postion是k,k需要和另外两个的位置不同
                    if k != l[0] and k != l[1]:
                        #res.append([k,l[0],l[1]])
                        l1 = sorted([nums[k],nums[l[0]],nums[l[1]]])
                        if l1 not in res:
                            res.append(l1)
        return res

#方法二
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cnt = collections.defaultdict(int)
        for n in nums:
            cnt[n] += 1
        keys = sorted(cnt.keys())
        res = []
        for i, a in enumerate(keys):
            # 处理相等的情况, cnt[a]-1是为了保证下面的b和c如果和a相等的话其cnt至少也需要为1
            cnt[a] -= 1
            for b in keys[i:]:
                if cnt[b] >= 1:
                    # 这里需要保证cnt[b]至少为1, 因为有可能a和b相等, 但是cnt[a]=1, 此时就不可以用b了
                    c = -a-b
                    if c < b:
                        # 剪枝优化, 后面的b更大, 意味着c更不满足c>=b了, 直接break即可
                        break
                    if c > b and cnt[c] >= 1 or c == b and cnt[b] >= 2:
                        # 去重考虑, 添加的三个数必须是非递减的关系
                        res.append([a, b, c])
        return res

nums = [-1, 0, 1, 2, -1, -4]
s1 = Solution()
print(s1.threeSum(nums))


