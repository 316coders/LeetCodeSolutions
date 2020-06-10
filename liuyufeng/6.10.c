
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

//方法一：递归法
//1,定位根节点
//2,根节点左边作为左支递归处理
//3,根节点右边作为右支递归处理

struct TreeNode* sortedArrayToBST(int* nums, int numsSize){
    int  iRoot = 0;
    struct TreeNode * pCurNode = NULL;
    if((NULL == nums ) || (0 == numsSize)) return NULL;
    pCurNode = (struct TreeNode*) malloc (sizeof (struct TreeNode));
    iRoot = numsSize/2;
    pCurNode->val = nums[iRoot];
    pCurNode->left = sortedArrayToBST(&nums[0], iRoot);
    pCurNode->right = sortedArrayToBST(&nums[iRoot +1], numsSize - iRoot -1);
    return pCurNode;
}