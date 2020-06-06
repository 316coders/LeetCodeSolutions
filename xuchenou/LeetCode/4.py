"""
4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """
            
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2



"""
#有问题，待修改
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #不会同时为空，就是可能1个为空
        l_nums1 = len(nums1)
        l_nums2 = len(nums2)
        all_length = l_nums1 + l_nums2
        if(l_nums1 == 0):
            if(l_nums2 % 2 == 0):
                return (nums2[int(l_nums2/2)-1] +nums2[int(l_nums2/2)])/2
            else:
                return nums2[int(l_nums2/2)]
        if(l_nums2 == 0):
            if(l_nums1 % 2 == 0):
                return float((nums1[int(l_nums1/2)-1] +nums1[int(l_nums1/2)]))/2
            else:
                return nums1[int(l_nums1/2)]
        #开始正常判断,统计总数,记录n1和n2的开始值，因为是有序的，用类似归并排序的方法。
        all_length = l_nums1 + l_nums2
        now_n1 = nums1[0]
        now_n2 = nums2[0]
        count = 0
        index_n1 = 0
        index_n2 = 0
        mid = all_length / 2
        if_odd = all_length % 2  # 如果是偶数就是 0=false
        #找到中位数,== 1 代表中位数只要最中间的那个。 == 0 则是需要两个数平均
        if(if_odd == 1):
            while(count < (mid - 0.5)):
                #双方没到底部
                if(index_n1 != l_nums1 - 1 and index_n2 != l_nums2 - 1):
                    if(now_n1 <= now_n2):
                        index_n1 += 1
                        count += 1
                        if count == mid - 0.5:
                            return float(now_n2)
                        now_n1 = nums1[index_n1]
                    else:
                        index_n2 += 1
                        count += 1
                        if count == mid - 0.5:
                            return float(now_n1)
                        now_n2 = nums2[index_n2]
                #nums1到底，之后去nums2找
                elif(index_n1 == l_nums1 - 1):
                    index_n2 += 1
                    count += 1
                    now_n2 = nums2[index_n2]
                    if count == mid - 0.5:
                        if(now_n1 <= now_n2):
                            return float(now_n1)
                        else:
                            return float(now_n2)
                else:
                    index_n1 += 1
                    count += 1
                    now_n1 = nums1[index_n1]
                    if count == mid - 0.5:
                        if(now_n1 <= now_n2):
                            return float(now_n1)
                        else:
                            return float(now_n2)

        else:
            while(count < mid):
                #双方没到底部
                if(index_n1 != l_nums1 - 1 and index_n2 != l_nums2 - 1):
                    if(now_n1 <= now_n2):
                        index_n1 += 1
                        count += 1
                        if count == mid :
                            return (now_n1 + now_n2) /2
                        now_n1 = nums1[index_n1]
                    else:
                        index_n2 += 1
                        count += 1
                        if count == mid :
                            return (now_n1 + now_n2) /2
                        now_n2 = nums2[index_n2]
                #nums1到底，之后去nums2找
                elif(index_n1 == l_nums1 - 1):
                    index_n2 += 1
                    count += 1
                    if count == mid :
                        return (now_n1 + now_n2) /2
                    now_n2 = nums2[index_n2]
                else:
                    index_n1 += 1
                    count += 1
                    if count == mid :
                        return (now_n1 + now_n2) /2
                    now_n1 = nums1[index_n1]
        return 0.0 


        
"""        
nums1 = [1, 3]
nums2 = [2]

nums3 = [1, 2]
nums4 = [3, 4]

nums5 = [3]
nums6 = [-2,-1]

nums7 = [1,2]
nums8 = [-1,3]

s1 = Solution()
#print(s1.findMedianSortedArrays(nums1,nums2))
#print(s1.findMedianSortedArrays(nums3,nums4))
#print(s1.findMedianSortedArrays(nums5,nums6))
print(s1.findMedianSortedArrays(nums7,nums8))