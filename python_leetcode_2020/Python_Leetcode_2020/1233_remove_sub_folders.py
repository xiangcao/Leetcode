"""
Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'
folder[i] always starts with character '/'
Each folder name is unique.
"""

class Solution1:
    #1.Sort the folders;
    #2. For each folder check if the followings are child folders; if yes, ignore; otherwise, count it in
    """
    the time compleixty is actually O(n * m * logn).
    Because the sort is based on merge sort for Object and time complexity of merge sort is O(n * logn). That means n * logn times comparing happened.
    For this question, it just makes the comparing time be O(m). Thus it won't increase the number of "layers" of merge sort to log(n * m).

    Time: O(n * m * log(n)), space: O(1)(excluding space cost of sorting part), where n = folder.length, m = average size of the strings in folder.

    """
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        folder.sort()
        for f in folder:
            if not ans or not f.startswith(ans[-1] + '/'): #need '/' to ensure a parent.
                ans.append(f)
        return ans
    

# solution 2; Each folder is a word;
# Each character of a folder path is a branch in trie, including '/'
# return the first prefix that's a complete word (folder) in each branch
# time complexity: O(n*m), n = len(folders);  m = average size of the strings in folders
class Trie:
    def __init__(self):
        self.sub = collections.defaultdict(Trie)
        self.index = -1

class Solution2:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.root = Trie()
        for i in range(len(folder)):
            cur = self.root
            for c in folder[i]:
                cur = cur.sub[c]
            cur.index = i
        return self.bfs(self.root, folder)
    def bfs(self, trie: Trie, folder: List[str]) -> List[str]:
        q, ans = [trie], []
        for t in q:
            if t.index >= 0:
                ans.append(folder[t.index])
            for c in t.sub.keys():
                if '/' != c or t.index < 0:
                    q.append(t.sub.get(c))
        return ans

# Solutio 3: Each folder is a word; 
# break each path into segments; each segment (multi-charcters) is Branch of Trie Node. 
# return the first prefix that's a complete word (folder) in each branch
# Much faster than solution 2
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            #if char not in node.children:
            #    node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True  
    
    def find(self):
        def dfs(direc, node):
            if node.isEnd:
                answer.append('/' + '/'.join(direc))
                return
            for char in node.children:
                dfs(direc + [char], node.children[char])
        
        answer = []
        dfs([], self.root)
        return answer


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            f = f.split('/')[1:]
            trie.insert(f)
        return trie.find()
