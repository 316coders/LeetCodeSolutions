# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        nex = None
        
        current = pHead
        while(current):
            nex = current.next  #nex = 2
            current.next = pre  #1的next = null
            pre = current    #pre从null移动到1
            current = nex    #current从1移动到2
        return pre