class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact=[1]
        for i in range(1,n+1):
            fact.append(fact[-1]*i)
        permu=[]
        eligible= range(n)
        for i in range(n):
            # 1th,2nd,3rd, ....., (n-1-i)!-th permutation  should all have 1 as the first digit. 
            digit = (k-1)/fact[n-1-i]
            permu.append( eligible[digit] + 1 )
            eligible.remove(eligible[digit])
            k = (k-1) % fact[n-1-i] + 1
        return ''.join([str(i) for i in permu])
