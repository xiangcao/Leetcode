"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
"""
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for c in word:
            node = node.children[c]
        node.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def searchInNode(word, node):
            for i, c in enumerate(word):
                if c != '.':
                    if c not in node.children:
                        return False
                    node = node.children[c]
                else:
                    for _, childnode in node.children.items():
                        if searchInNode(word[i+1:], childnode):
                            return True
                    return False
                        
            return node.word
        return searchInNode(word, self.trie)
