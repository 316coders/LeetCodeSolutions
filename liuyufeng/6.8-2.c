// 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

// 示例 1:

// 输入: 1->1->2
// 输出: 1->2
// 示例 2:

// 输入: 1->1->2->3->3
// 输出: 1->2->3

//方法一：删除链表中的元素
struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode*    pCurNode    = head;
    struct ListNode*    pNextNode   = head;

    if(NULL == head) return head;

    pNextNode = pCurNode->next;
    while(pNextNode != NULL)
    {
        if(pCurNode->val == pNextNode->val)
        {
            pNextNode = pNextNode->next;
            pCurNode->next = pNextNode;
        }
        else
        {
            pCurNode = pNextNode;
            pNextNode = pNextNode->next;
        }
    }
    return head;
}

