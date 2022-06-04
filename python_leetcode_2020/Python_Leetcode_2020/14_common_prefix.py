"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0) return "";
    for (int i = 0; i < strs[0].length() ; i++){
        char c = strs[0].charAt(i);
        for (int j = 1; j < strs.length; j ++) {
            if (i == strs[j].length() || strs[j].charAt(i) != c)
                return strs[0].substring(0, i);             
        }
    }
    return strs[0];
}

Further Thoughts / Follow up
Given a set of keys S=[S1,S2,..,Sn], find the longest common prefix among a string q and S. This LCP query will be called frequently.

We could optimize LCP queries by storing the set of keys S in a Trie. For more information about Trie, please see this article Implement a trie (Prefix trie). In a Trie, each node descending from the root represents a common prefix of some keys. But we need to find the longest common prefix of a string q and all key strings. This means that we have to find the deepest path from the root, which satisfies the following conditions:

1: it is prefix of query string q
2: each node along the path must contain only one child element. Otherwise the found path will not be a common prefix among all strings.
3: the path doesn't comprise of nodes which are marked as end of key. Otherwise the path couldn't be a prefix a of key which is shorter than itself.
Algorithm


Trie
Complexity Analysis

In the worst case query qq has length mm and it is equal to all nn strings of the array.

Time complexity : preprocessing O(S)O(S), where SS is the number of all characters in the array, LCP query O(m)O(m).

Trie build has O(S)O(S) time complexity. To find the common prefix of qq in the Trie takes in the worst case O(m)O(m).

Space complexity : O(S)O(S). We only used additional SS extra space for the Trie.

