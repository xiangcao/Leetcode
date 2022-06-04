class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]	


Java code:
Binary Search:

We do binary search on the duplicate substring length, for example if we know a length 10 substring has duplicate, then there is no need to test any substring with length smaller than 10 right?

Rolling Hash:
Take this string "12121" as an example, we want to find out whether we have duplicate substring with length 3:

A simple hash computation for its 1st 3 character substring "121" would be 1*10^2 + 2*10^1 + 1*10^0 = 121 (basically we used its decimal value as its unique hash in this example)
For 2nd substring "212" would be (121 - 1*10^2) * 10 + 2 * 10^0 = 212
For 3rd substring "121" would be (212 - 2*10^2) * 10 + 1 * 10^0 = 121 and we now have a collision!

Did you notice the hash computation is constant time for each substring? That's the key of this algorithm, we can use previous substring's hash to compute the current substring's hash because current substring is simply previous substring with first character removed and new character added to the end.

Princeton's JAVA code on RabinKarp: https://algs4.cs.princeton.edu/53substring/RabinKarp.java.html

class Solution {
    private static final long q = (1 << 31) - 1;
    private static final long R = 256;
        
    public String longestDupSubstring(String S) {      
        int left = 2;
        int right = S.length() - 1;
        int start = 0;
        int maxLen = 0;
        
        while (left <= right) {
            int len = left + (right - left) / 2;
            boolean found = false;
            
            Map<Long, List<Integer>> map = new HashMap<>();
            long hash = hash(S, len);
            map.put(hash, new ArrayList<>());
            map.get(hash).add(0);
            long RM = 1l;
            for (int i = 1; i < len; i++) RM = (R * RM) % q;
            
            loop:
            for (int i = 1; i + len <= S.length(); i++) {
                hash = (hash + q - RM * S.charAt(i - 1) % q) % q;
                hash = (hash * R + S.charAt(i + len - 1)) % q;
                if (!map.containsKey(hash)) {
                    map.put(hash, new ArrayList<>());
                } else {
                    for (int j : map.get(hash)) {
                        if (compare(S, i, j, len)) {
                            found = true;
                            start = i;
                            maxLen = len;
                            break loop;
                        }
                    }
                }
                map.get(hash).add(i);
            }
            if (found) left = len + 1;
            else right = len - 1;
        }
        
        return S.substring(start, start + maxLen);
    }
    
    private long hash(String S, int len) { 
        long h = 0;
        for (int j = 0; j < len; j++) h = (R * h + S.charAt(j)) % q;
        return h;
    }
    
    private boolean compare(String S, int i, int j, int len) {
        for (int count = 0; count < len; count++) {
            if (S.charAt(i++) != S.charAt(j++)) return false ; 
        }
        return true ; 
    }
}
