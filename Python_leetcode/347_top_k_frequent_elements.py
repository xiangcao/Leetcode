class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        
        return [res[0] for res in counter.most_common(k)]
        
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        frequency= collections.defaultdict(list)
        
        for key in counter:
            frequency[counter[key]] += [key]
            
        result=[]
        for freq in range(len(nums), 0, -1):
            if len(result) >= k:
                return result
            result.extend(frequency[freq])
        return result

    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        priorityQ = []
        result=[]
        for key in counter:
            heapq.heappush(priorityQ, (-1*counter[key], key))
            if len(priorityQ) > len(counter) - k:
                result.append(priorityQ[0][1])
                heapq.heappop(priorityQ)
        return result
    
