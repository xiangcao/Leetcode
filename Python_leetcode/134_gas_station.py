class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum = 0
        length = len(gas)
        tempSum = 0
        i, j =0, -1
        while i < length:
            sum += gas[i]-cost[i]
            tempSum += gas[i]-cost[i]
            if tempSum < 0:
                tempSum = 0
                j = i
            i += 1
        if sum < 0:
            return -1
        return j+1
                
