"""
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
"""
# The first idea is to add all input words in the trie and then implement a standard search.
# The problem is we don't know how many characters to match. On the example above, should we try to match the last three stream characters "jkl", the last two "kl", or the last one "l"?
# The way to solve the problem is to notice that we always know the last character to match. That gives us an idea to build a trie of reversed words, and try to match the reversed stream of characters.
# This way, instead of multiple choices to match, we always have one path: to match character by character starting from the end of the stream. We could stop once we meet the "end of word" label, which means success. If we couldn't match a character before we meet that label, that means fail.
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.stream = collections.deque([])
        for w in set(words):
            node = self.trie
            for c in w[::-1]:
                node = node.children[c]
            node.word = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for c in self.stream:
            if c not in node.children:
                return False
            node = node.children[c]
            if node.word: return True
        return node.word

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
