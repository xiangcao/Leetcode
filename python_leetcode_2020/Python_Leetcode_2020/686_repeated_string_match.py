iGiven two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".

1 <= a.length <= 104
1 <= b.length <= 104
a and b consist of lower-case English letters.

This is basically a modified version of string find, which does not stop at the end of A, but continue matching by looping through A.
"""


class Solution(object):
    # test case: 'a', 'aa'
    # time limit exceeded.
    # c++ version of this solution took 1216 ms and passed, faster than 7%
    def repeatedStringMatch1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        for i in range(len(a)):
            j = 0
            while j < len(b):
                if a[(i+j) % len(a)] == b[j]:
                    j += 1
                    continue
                else:
                    break
            if (j == len(b)):
                return (i + j - 1 ) / len(a) + 1
        return -1
"""
Intuition

The question can be summarized as "What is the smallest k for which B is a substring of A * k?" We can just try every k.

Algorithm

Imagine we wrote S = A+A+A+.... If B is to be a substring of S, we only need to check whether some S[0:], S[1:], ..., S[len(A) - 1:] starts with B, as S is long enough to contain B, and S has period at most len(A).

Now, suppose q is the least number for which len(B) <= len(A * q). We only need to check whether B is a substring of A * q or A * (q+1). If we try k < q, then B has larger length than A * q and therefore can't be a substring. When k = q+1, A * k is already big enough to try all positions for B; namely, A[i:i+len(B)] == B for i = 0, 1, ..., len(A) - 1.

Runtime: 108 ms, faster than 56.68% of Python3 online submissions for Repeated String Match.
Time Complexity: O(N*(N+M)), where M, N are the lengths of strings A, B. We create two strings A * q, A * (q+1) which have length at most O(M+N). When checking whether B is a substring of A, this check takes naively the product of their lengths.

"""

    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1                 


    # 100 ms, faster than 74.72%
    # len(A): M, len(B): N
    # O(N * (M+N))
    # space: O(M+N)
    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1
    
    # Rolling Hash
    # Time O(M+N)
    # Space: O(1)
    def repeatedStringMatch(self, A, B):
        def check(index):
            return all(A[(i + index) % len(A)] == x
                       for i, x in enumerate(B))

        q = (len(B) - 1) // len(A) + 1

        p, MOD = 113, 10**9 + 7
        p_inv = pow(p, -1) # p_inv = pow(p, MOD-2, MOD)
        power = 1

        b_hash = 0
        for x in map(ord, B):
            b_hash += power * x
            b_hash %= MOD
            power = (power * p) % MOD

        a_hash = 0
        power = 1
        for i in xrange(len(B)):
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            power = (power * p) % MOD

        if a_hash == b_hash and check(0): return q

        power = (power * p_inv) % MOD
        for i in xrange(len(B), (q+1) * len(A)):
            a_hash = (a_hash - ord(A[(i - len(B)) % len(A)])) * p_inv
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            if a_hash == b_hash and check(i - len(B) + 1):
                return q if i < q * len(A) else q+1

        return -1
