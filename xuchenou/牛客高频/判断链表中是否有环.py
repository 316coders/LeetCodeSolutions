# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return bool布尔型
#
class Solution:
    def hasCycle(self , head ):
        # write code here
        #方法一:每过一个链表将其值设置为特殊数,下次遇到该特殊数就是有环,到底无环
        #方法二:快慢指针,相遇有环
        fast = head
        slow = head
        while(fast!= None and fast.next != None):
            #快的走两步
            fast = fast.next.next
            slow = slow.next
            if(slow == fast):
                return True
        return False