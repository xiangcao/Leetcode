class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = 0, 1
        count1 = count2 = 0
        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = nums[i], 1
            elif count2 == 0:
                candidate2, count2 = nums[i], 1
            else:
                count1, count2 = count1-1, count2-1
        return [n for n in [candidate1, candidate2] if nums.count(n) > len(nums) //3 ]

"""
Solution

I keep up to two candidates in my counter, so this fulfills the O(N) time and O(1) space requirements.

def majorityElement(self, nums):
    ctr = collections.Counter()
    for n in nums:
        ctr[n] += 1
        if len(ctr) == 3:
            ctr -= collections.Counter(set(ctr))
    return [n for n in ctr if nums.count(n) > len(nums)/3]
Explanation

Think of it this way: Find three different votes and hide them. Repeat until there aren't three different votes left. A number that originally had more than one third of the votes now still has at least one vote, because to hide all of its votes you would've had to hide more than three times one third of the votes - more votes than there were. You can easily have false positives, though, so in the end check whether the remaining up to two candidates actually had more than one third of the votes.

My code does just that: Collect (count) the votes for every number, but remove triples of three different votes on the fly, as soon as we have such a triple.

Generalization to ⌊N/k⌋, still O(N) time but O(k) space

For the general problem, looking for elements appearing more than ⌊N/k⌋ times for some positive integer k, I just have to change my 3 to k. Then it already works and takes takes O(k) space and O(kN) time.

The O(kN) time does not come from the main loop, though. Yes, each ctr -= ... does cost k, but I only have to do it at most N/k times. To put it in terms of the above explanation, I can't hide a vote more than once.

No, the culprit is my last line, counting each remaining candidate separately. If I count them at the same time, I get O(N) again. Here's the full generalized code:
"""
def majorityElement(self, nums, k):
    ctr = collections.Counter()
    for n in nums:
        ctr[n] += 1
        if len(ctr) == k:
            ctr -= collections.Counter(set(ctr))
    ctr = collections.Counter(n for n in nums if n in ctr)
    return [n for n in ctr if ctr[n] > len(nums)/k]
