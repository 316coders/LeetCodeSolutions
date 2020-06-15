"""
5188. 树节点的第 K 个祖先
给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。

请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。

树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。



示例：
输入：
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

输出：
[null,1,0,-1]

解释：
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
 

提示：
1 <= k <= n <= 5*10^4
parent[0] == -1 表示编号为 0 的节点是根节点。
对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
0 <= node < n
至多查询 5*10^4 次

"""
from typing import List
class TreeAncestor:
    parent = list()
    k_tree = 2
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.k_tree = self.getKtree(self.parent)

    def getKtree(self,nums: List[int]) -> int:
        d1 = dict()   #{4: 1, 3: 3, 1: 2, 2: 1}
        for i in self.parent:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        d2 = sorted(d1.items(),key = lambda item:item[1])
        #print(d2[-1][1])
        return(d2[-1][1])

    def getKthAncestor(self, node: int, k: int) -> int:
        #n叉树
        n = self.k_tree
        while k >= 1:
            if node == 0:
                return -1                
            node = int((node - 1) / n)
            #node = int(node / n)
            k -= 1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

s1 = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(s1.getKthAncestor(3,1))
print(s1.getKthAncestor(5,2))
print(s1.getKthAncestor(6,3))
 
s2 = TreeAncestor(5,[-1,0,0,0,3])
print(s2.getKthAncestor(1,5))
print(s2.getKthAncestor(3,2))
print(s2.getKthAncestor(0,1))
print(s2.getKthAncestor(3,1))
print(s2.getKthAncestor(3,5))
#预期：[null,-1,-1,-1,0,-1]
#输出：[null,-1,0,-1,1,-1]

s3 = TreeAncestor(10,[-1,0,0,1,2,0,1,3,6,1])
print(s3.getKthAncestor(8,6))
print(s3.getKthAncestor(9,7))
print(s3.getKthAncestor(1,1))
print(s3.getKthAncestor(2,5))
print(s3.getKthAncestor(4,2))
print(s3.getKthAncestor(7,3))#
print(s3.getKthAncestor(3,7))
print(s3.getKthAncestor(9,6))
print(s3.getKthAncestor(3,5))
print(s3.getKthAncestor(8,8))

#预期:[null,-1,-1,0,-1,0,0,-1,-1,-1,-1]
#输出[null,-1,-1,0,-1,-1,-1,-1,-1,-1,-1]

#输出2[null,-1,-1,0,-1,0,-1,-1,-1,-1,-1]