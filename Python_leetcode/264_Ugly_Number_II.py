class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
    def nthUglyNumber(self, n):
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            m2, m3, m5 = q[i2] * 2, q[i3] * 3, q[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q += [m]
        return q[-1]


#注意以下程序的bug
#input n = 7
#result : [1, 2, 3, 4, 5, 6, 6]. 
#why will it get a wrong result? 

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1]
        i2 = i3 = i5 = 0
        while len(result) < n:
            m1, m2, m3 = result[i2] * 2, result[i3] * 3, result[i5]*5
            m = min(m1,m2,m3)
            if m == m1:
                i2 += 1
            elif m == m2:
                i3 += 1
            elif m == m3:
                i5 += 1
            result += [m]
        print result
        return result[-1]
