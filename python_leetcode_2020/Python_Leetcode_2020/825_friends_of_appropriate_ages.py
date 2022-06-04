"""
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?
"""

class Solution:
    # binary search: Time O(nlogn), Space O(1)
    def numFriendRequests_1(self, ages: List[int]) -> int:
        #0.5 a + 7 < a ==> 7 < 0.5a ==> 14 < a
        #0.5 a + 7 > a ==> 7 > 0.5a ==> 14 > a
        
        #Age(A) > 14
        # 0.5*Age(A)+7 < Age(B) <= Age(A)
        
        ages.sort()
        count = 0
        j = bisect.bisect_right(ages, 14)
        for a in range(j, len(ages)):
            lower_boundary = ages[a] * 0.5 + 7 
            first_b_friend = bisect.bisect_right(ages, lower_boundary, 0, a+1)
            # A make request to person with smaller age on the left
            count += a - first_b_friend
            # A make request to person on the right with same age
            count += bisect.bisect_right(ages, ages[a]) - a - 1
        
        return count

    # count sort Time O(n), space O(1)
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        numInAge,sumInAge = [0] * 121, [0] * 121

        for i in ages:
            numInAge[i] += 1
        
        for i in range(1, 121):
            sumInAge[i] = numInAge[i] + sumInAge[i - 1]
        
        for i in range(15, 121):
            if(numInAge[i] == 0):
                continue
            count = sumInAge[i] - sumInAge[i // 2 + 7] 
            res += count * numInAge[i] - numInAge[i]  #people will not friend request themselves, so  - numInAge[i]
        return res
