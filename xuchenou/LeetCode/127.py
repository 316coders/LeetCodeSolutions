"""
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) ->  int:
        #去重
        wordList = set(wordList)
        #如果 endword 不在字典中,返回[]
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)
        length = len(beginWord)
        letters = set('abcdefghijklmnopqrstuvwxyz')
        #设定初始步长为2
        step = 2
        forward = {beginWord}
        backward = {endWord}
        #开始bfs
        while(forward):
            if len(forward) > len(backward):
                #交换集合,使得每次都从小集合开始遍历,减少时间        
                forward,backward = backward,forward
            cur = set()
            for word in forward:
                for i in range(length):
                    x = word[:i]
                    y = word[i+1:]
                    for l in letters:
                        #将单词从range(0,length),每一位都替换从 a 到 z 检查是否是endword 和 是否在图中(wordlist)有
                        temp = x + l + y
                        if temp in wordList:
                            return step
                        if temp in wordList:
                            cur.add(temp)
                            wordList.remove(temp)
            step += 1
            #新遍历出来的作为下次遍历的新一层forward
            forward = cur
        return 0


"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) ->  int:
        wordList = set(wordList)  # 去除wordList中的重复词
        if endWord not in wordList: return 0  # endWord不在wordList中，无法转换
        if beginWord in wordList: wordList.remove(beginWord)  # beginWord在wordList中，移出单词表
        res,forward,backward= 2,{beginWord},{endWord}
        letters,length = set('abcdefghijklmnopqrstuvwxyz'),len(endWord)
        while forward:
            if len(forward) > len(backward):
                forward,backward = backward,forward#交换后每次都从小集合中遍历
            cur = set()#相当于层次序遍历中的新一层，保存的是每一步交换后的单词
            for word in forward:
                for idx in range(length):
                    x,y = word[:idx],word[idx+1:]
                    for letter in letters:
                        temp = x + letter + y  # 将每个单词的每个位置更换一个字母（a-z），看在不在backward中，在的话即等于endWord，返回res
                        if temp in backward: return res
                        if temp in wordList:
                            cur.add(temp)#这里将与forward中单词只差一个字母的有效单词加入，因为该题只要求最短距离，所以已达到的都删除，避免重复访问。连visited数组都省下了
                            wordList.remove(temp)
            res += 1
            forward = cur
        return 0

beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

s1 = Solution()
print(s1.ladderLength(beginWord,endWord,wordList))