class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    # clrs qsort
    def removeElement(self, A, elem):
        j = len(A)-1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j+1

    def removeElement_(self, A, elem):
        k = 0 
        for i in A:
            if i != elem:
                A[k] = i
                k+=1
        return k



sol = Solution()
import time
A=[3,5,1,2,7,2,8,9,10,11,2]
elem=2
t1 = time.time()
for i in range(1000):
    sol.removeElement(A, elem)
print "time spent: %f" % (time.time()-t1)


