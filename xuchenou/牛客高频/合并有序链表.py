#将两个有序的链表合并为一个新链表，要求新的链表是通过拼接两个链表的节点来生成的。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param l1 ListNode类 
# @param l2 ListNode类 
# @return ListNode类
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self , l1 , l2 ):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next
                
                
