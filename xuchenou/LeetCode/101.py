"""
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = collections.deque()
        queue.append((root, root))
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True
