"""
126. 单词接龙 II
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
"""
#分析
#如果endword 不在字典中,返回[]   beginWord 和 endWord 是非空的，且二者不相同。
#每次转换只能改变一个字母。转换过程中的中间单词必须是字典中的单词。
#所有单词具有相同的长度。

#栈的解法思考
#使用堆栈解决试试看,首先将 hit, 与首字母h不同\其他与h相同的全部入栈,然后list中减去这些.()
# *it在数组中不存在,栈空,那就开始将 hit,与第二个字母i不同的入栈
# h*t 有 hot,出栈hot,*ot  过于复杂

#图的解法思考
#还是用图吧,每个单词是一个点,一个字母不同的单词之间有连线.  看beginword 与 endword 是否连通.
#图的bfs遍历,但是需要优化实践复杂度.
#改为双向BFS,需要从beginWord 到endWord,同时也是需要从endWord 到 beginword
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

###参见127题目代码的写法,这里记录个其他大佬写的 hash表+双bfs优化方法.
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if not endWord in wordList:
            return []
        hash=collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hash[word[:i]+"*"+word[i+1:]].append(word)
        def edges(word):
            for i in range(len(word)):
                for newWord in hash[word[:i]+'*'+word[i+1:]]:
                    if not newWord in marked:
                        yield newWord
        def findPath(end):
            res=[]
            for curr in end:
                for parent in path[curr[0]]:
                    res.append([parent]+curr)
            return res
        marked=set()
        path=collections.defaultdict(set)
        begin=set([beginWord])
        end=set([endWord])
        forward=True
        while begin and end:
            if len(begin)>len(end):
                begin,end=end,begin
                forward=not forward
            temp=set()
            for word in begin:
                marked.add(word)
            for word in begin:
                for w in edges(word):
                    temp.add(w)
                    if forward:
                        path[w].add(word)
                    else:
                        path[word].add(w)
            begin=temp
            if begin&end:
                res=[[endWord]]
                while res[0][0]!=beginWord:
                    res=findPath(res)
                return res
        return []

作者：Mcdull0921
链接：https://leetcode-cn.com/problems/word-ladder-ii/solution/cong-bfssi-xiang-kai-shi-de-jin-hua-zhi-lu-2400msy/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
