"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""

class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word = -1
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        root = Trie()
       
        for index, w in enumerate(words):
            cur = root
            for c in w:
                 cur = cur.children[c]
            cur.word = index
        
        stack=[root]
        ans = ""
        while stack:
            cur = stack.pop()
            if cur.word >= 0 or cur == root:
                if cur != root:
                    word = words[cur.word]
                    if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                        ans = word
                    
                for neighbor in cur.children.values():
                    stack.append(neighbor)
        return ans
