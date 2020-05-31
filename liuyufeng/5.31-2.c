
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 解题思路：首先根节点为空的话即是对称的。

整个树对称，要求根节点的左子树与右子树对称。那么如何判断左右子树对称？需要左子树的左子树和右子树的右子树对称，
同时左子树的右子树和右子树的左子树对称。由此得到递归函数。

递归函数中，先判断边界条件。若左右子树同时为空，是对称的。若左右子树只有一个为空，是不对称的。
需要满足3个判断条件则左右子树是对称的
1 左右子树的值相等；
2 左子树的左子树和右子树的右子树对称，调用递归函数；
3 左子树的右子树和右子树的左子树对称，调用递归函数。
这里为了看起来方便，分开写出来即可。

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool recursion(struct TreeNode* left, struct TreeNode* right) {
    if(left == NULL && right == NULL) {
        return true;
    }else if(left == NULL || right == NULL) {
        return false;
    }

    bool c1 = (left->val == right-> val);
    bool c2 = recursion(left->left, right->right);
    bool c3 = recursion(left->right, right->left);
    if (c1 && c2 && c3) {
        return true;
    }else {
        return false;
    }
}
bool isSymmetric(struct TreeNode* root){
    if (root == NULL) {
        return true;
    }
    return recursion(root->left, root->right);
}