"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = collections.deque([beginWord])
        wordList = set(wordList)
        distance = 1
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur == endWord:
                    return distance
                for j in range(len(cur)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = cur[:j] + c + cur[j+1:]
                        if nextWord in wordList:
                            wordList.remove(nextWord)
                            queue.append(nextWord)
            distance += 1
        return 0
    
    # store distance together with each word in the queue
    # this way, we do not need to visit nodes level by level in bfs
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
    
    # my solution 4 years ago. almost the same as solution 1 above but better readability
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        toVisit = collections.deque([beginWord])
        
        distance = 1
        
        def addNextWords(curWord):
            for i in range(len(curWord)):
                for k in range(26):
                    k = chr(ord('a')+k)
                    nextWord = curWord[:i] + k + curWord[i+1:]
                    if nextWord in wordList or nextWord == endWord:
                        toVisit.appendleft(nextWord)
                        wordList.discard(nextWord)
            
                        
        while toVisit:
            curLevelSize = len(toVisit)
            
            for i in range(curLevelSize):
                word = toVisit.pop()
                if word == endWord:
                    return distance
                    
                addNextWords(word)
                
            distance += 1
        return 0
