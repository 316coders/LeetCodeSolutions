from typing import List
import functools
#题目定义的stronger比较方法
mid = 0
def is_stronger(i: int,j: int):
    if(abs(i-mid) > abs(j-mid)):
        return True
    if(abs(i-mid) == abs(j-mid) and i > j):
        return True
    return False
#获得数组中位数的方法
def get_mid(arr: List[int]):
    length = len(arr)
    return arr[int(((length - 1) / 2))]


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr2 = sorted(arr)
        global mid
        mid = get_mid(arr2)
        print(mid)
        length = len(arr2)
        sorted_arr = list()
        #完成stronger排序。
        sorted_arr.append(arr2[0])
        #如果长度1直接返回
        if(length == 1):
            return sorted_arr

        #从第二个开始排序
        for i in arr2[1:]:
            count = 0
            #对于arr中的每一个元素，插入时候与sorted_arr中已有的元素比较
            for j in sorted_arr:
                #如果i比j stronger ，返回true，否则false
                if(i == j):
                    sorted_arr.insert(count,i)
                    break
                if(is_stronger(i,j)):
                    sorted_arr.insert(count,i)
                    break
                count += 1
            #判断到sorted_arr的最后一个元素了还不是，就插入在尾端
            if(count == len(sorted_arr)):
                sorted_arr.append(i) 
        #sorted_arr = sorted(arr2, key=functools.cmp_to_key(is_stronger))
        return sorted_arr[0:k]
        #return sorted_arr

arr = [1,2,3,4,5]
k = 2

arr2 = [1,1,3,5,5]
k2 = 2

arr3 = [6,7,11,7,6,8]
k3 = 5

arr4 = [6,-3,7,2,11]
k4 = 3

arr5 = [-7,22,17,3]
k5 = 2
 
s1 = Solution()
print(s1.getStrongest(arr,k))
print(s1.getStrongest(arr2,k2))
print(s1.getStrongest(arr3,k3))
print(s1.getStrongest(arr4,k4))
print(s1.getStrongest(arr5,k5))


