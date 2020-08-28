"""
设计LRU缓存结构，该结构在构造时确定大小，假设大小为K，并有如下两个功能
set(key, value)：将记录(key, value)插入该结构
get(key)：返回key对应的value值

[要求]
set和get方法的时间复杂度为O(1)
某个key的set或get操作一旦发生，认为这个key的记录成了最常使用的。
当缓存的大小超过K时，移除最不经常使用的记录，即set或get最久远的。

若opt=1，接下来两个整数x, y，表示set(x, y)
若opt=2，接下来一个整数x，表示get(x)，若x未出现过或已被移除，则返回-1
对于每个操作2，输出一个答案

示例1
输入
[[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
输出
[1,-1]
"""

#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
import collections

class Solution:
    def LRU(self , operators , k ):
        d1 = collections.OrderedDict()
        length = k
        res = list()
        for i in operators:
            #如果 opt=1
            if i[0] == 1:
                if i[1] in d1:
                    d1.pop(i[1])
                    d1[i[1]] = i[2]
                if i[1] not in d1:
                    if(len(d1) == length):
                        d1.popitem(last = False)
                    d1[i[1]] = i[2]                       
            #如果 opt=2
            if i[0] == 2:
                if i[1] not in d1:
                    res.append(-1)
                else:
                    value = d1[i[1]]
                    d1.pop(i[1])
                    d1[i[1]] = value
                    res.append(value)
        return res
        
s1 = Solution()
input1 = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]]
input2 = 3
print(s1.LRU(input1,input2))