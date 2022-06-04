"""
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 
"""

class Trie:
    def __init__(self):
        self.sub = collections.defaultdict(Trie)
        self.suggestion = []
        
class Solution(object):
    """
    Sorting and searching cost O(n * m * log n) and O(L * m * logn), respectively; Therefore,
Time: O((n + L) * m * logn), space: O(L * m) - - including return list ans, but excluding space cost of sorting, where m = average length of products, n = products.length, L = searchWord.length().
    56 ms
"""
    def suggestedProducts1(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        ans = []
        cur = ''
        for i in range(len(searchWord)):
            cur += searchWord[i]
            i = bisect.bisect_left(products, cur)
            ans.append([p for p in products[i:i+3] if p.startswith(cur)])
        return ans
                   
    """
Complexity depends on the sorting, the process of building Trie and the length of searchWord. Sorting cost time O(m * n), due to involving comparing String, which cost time O(m) for each comparison, building Trie cost O(m * n). Therefore,
Time: O(m * n + L), space: O(m * n + L * m) - including return list ans, where m = average length of products, n = products.length, L = searchWord.length().
    264 ms
    """
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        root = Trie()
        for product in products:
            self._insert(product, root)
        return self._search(searchWord, root)

    def _insert(self, product, root):
        trie = root
        for char in product:
            trie = trie.sub[char]
            trie.suggestion.append(product)
            trie.suggestion.sort()
            if len(trie.suggestion) > 3:
                 trie.suggestion.pop()

    def _search(self, searchWord, root):
        ans = []
        for char in searchWord:
            if not root:
                return
            root = root.sub[char]
            ans.append(root.suggestion if root else [])
        return ans
