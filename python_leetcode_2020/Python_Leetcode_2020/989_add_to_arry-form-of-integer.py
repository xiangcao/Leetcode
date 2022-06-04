"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
"""

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        return A
    
    # avoid overflow (in non-python)
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        for i in reversed(range(len(A))):
            K, d = divmod(K, 10)
            carry, A[i] = divmod(A[i] + d, 10)
            K += carry
            if not K: break 
        if K: A = list(map(int, str(K))) + A
        return A


# avoid overflow 
class Solution {
    // avoid overflow
    public List<Integer> addToArrayForm(int[] A, int K) {
               List<Integer> result = new ArrayList<>();
        int i = A.length - 1, carry = 0;
        while (i >= 0 || K > 0) {
            int sum = carry;
            if (i >= 0) {
                sum += A[i];
            }
            if (K > 0) {
                sum += K % 10;
            }
            
            result.add(sum % 10);
            carry = sum / 10;
            
            i--;
            K /= 10;
        }
        
        if (carry == 1) {
            result.add(1);
        }
        
        Collections.reverse(result);
        return result; 
    }
}
