class Solution(object):
    #Accepted
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] * (rowIndex+1)
        prev = [1] * (rowIndex+1)
        
        for i in range(1, rowIndex+1):
            result[0] = result[i] = 1 
            for j in range(1, i):
                result[j] = prev[j-1] + prev[j]
            prev = copy.deepcopy(result)
        return result
       
    # Wrong 
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        result = [0] * (rowIndex+1)
        result[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(1, i+1):
                result[j] = result[j-1] + result[j]
        return result
        
    # Accepted. Best solution
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rty
        """
        result = [0] * (rowIndex+1)
        result[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                result[j] = result[j-1] + result[j]
        return result
        
        
    def factor(self, n):
        if(n <= 0):
            return 1
        factor = 1
        while(n > 0):
            factor *= n
            n -= 1
        return factor

    def getRow_(self, RowIndex):
        """
        :type RowIndex: int
        :rtype: List[List[int]]
        """
        n = RowIndex
        if(n == 0):
            return [1]
        List = [1] * (n + 1)
        for j in range(0, n + 1):
            if(n == j):
                List[j] = 1 
            elif(j == 0):
                List[j] = 1
            elif(j == 1):
                List[j] = n
            else:
                List[j] = self.factor(n) // (self.factor(j) * self.factor(n - j))

        return List
