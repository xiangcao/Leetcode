class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        result = []
        toVisit = set([beginWord])  #toVisit = collections.deque([beginWord])
        nextToVisit = set()
        father = collections.defaultdict(list)
        found = False
        
        def addNextWords(curWord):
            for i in range(len(curWord)):
                for k in range(26):
                    k = chr(ord('a')+k)
                    nextWord = curWord[:i] + k + curWord[i+1:]
                    if nextWord in wordlist or nextWord == endWord:
                        nextToVisit.add(nextWord)   #toVisit.appendleft(nextWord)
                        father[nextWord].append(curWord)
            
        while toVisit and not found:
            curLevelSize = len(toVisit)
            if endWord in toVisit:
                found = True
                break
            for word in toVisit:
                wordlist.discard(word)
            for word in toVisit:
                addNextWords(word)
            """for i in range(curLevelSize):
                word = toVisit.pop()
                addNextWords(word)
            """
            toVisit, nextToVisit = nextToVisit, set()

        def genPath(father, curPath, word):
            if word == beginWord:
                result.append([word]+curPath)
            else:
                for prevWord in father[word]:
                    genPath(father, [word] + curPath, prevWord)

        if found:
            genPath(father, [], endWord) 
        
        return result
        
