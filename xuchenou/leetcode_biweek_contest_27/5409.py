"""
5409. 检查一个字符串是否包含所有长度为 K 的二进制子串 显示英文描述 
给你一个二进制字符串 s 和一个整数 k 。
如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 True ，否则请返回 False 。


"""
#coding=utf-8
def kmp_match(s, p):
    m = len(s)
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:     #只去匹配前m-n个
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:           #for 循环中，如果没有从任何一个 break 中退出，则会执行和 for 对应的 else
                        #只要从 break 中退出了，则 else 部分不执行。
            return True
    return False


# 部分匹配表
def partial_table(p):
    '''''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret

def generate_binary(n):

  # 2^(n-1)  2^n - 1 inclusive
  bin_arr = range(0, int(pow(2,n)))
  bin_arr = [bin(i)[2:] for i in bin_arr]

  # Prepending 0's to binary strings
  max_len = len(max(bin_arr, key=len))
  bin_arr = [i.zfill(max_len) for i in bin_arr]

  #print(bin_arr)

  return bin_arr

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        arr = generate_binary(k)
        for i in arr:
            if not kmp_match(s,i):
                return False
        return True
                




#print (kmp_match("00110110", "00"))
#print (kmp_match("00110110", "110111"))

s1 = Solution()
s1.hasAllCodes("00110110",2)
  
