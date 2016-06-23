class Solution(object):
    #wrong. time-limit exceeded. duplicate result.
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        for i in range(2, n):
            if n % i == 0:
                if n/i < i: 
                    break
                factor1 = [i] + self.getFactors(i)
                factor2 = [n/i] + self.getFactors(n/i)
                for i in factor1:
                    for j in factor2:
                        result.append([i,j])
        return result

       table={}

#the three methods below can be modified to be accepted with a simple fixes below. during interview, use the last two method. 
    #correct memory limit out
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n in self.table:
            return self.table[n]
        result=set()
        for i in range(2, n):
            if n % i == 0:
                if n/i < i: 
                    break
                factor1 = [[i]] + self.getFactors(i)
                factor2 = [[n/i]] + self.getFactors(n/i)
                for i in factor1:
                    for j in factor2:
                        result.add(tuple(sorted((i+j))))
        self.table[n] = [list(i) for i in result]
        return self.table[n]


    # wrong. memory limit 23848713.duplicate result
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(start, n):
            result=[]
            for i in range(start, n):
                if n % i == 0:
                    if n/i < i: 
                        break
                    factor1 = [[i]] + helper(start,i)
                    factor2 = [[n/i]] + helper(i,n/i)
                    for i in factor1:
                        for j in factor2:
                            result.append(sorted((i+j)))
            return result
        return helper(2, n)

    #correct. mmeory limit exceeded
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(result, path, start, n):
            for i in range(start, n):
                if n % i == 0:
                    if n/i < i: 
                        break
                    newPath = path+[i]
                    helper(result, newPath, i,n/i)
                    newPath += [n/i]
                    result.append(newPath)
        result =[]
        path=[]
        helper(result, path, 2, n)
        return result


#three accepted.
    #accepted
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n in self.table:
            return self.table[n]
        result=set()
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                factor1 = [[i]] 
                factor2 = [[n/i]] + self.getFactors(n/i)
                for i in factor1:
                    for j in factor2:
                        result.add(tuple(sorted((i+j))))
        self.table[n] = [list(i) for i in result]
        return self.table[n]
    
    #accepted
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(start, n):
            result=[]
            for i in range(start, int(math.sqrt(n))+1):
                if n % i == 0:
                    factor1 = [[i]]
                    factor2 = [[n/i]] + helper(i,n/i)
                    for i in factor1:
                        for j in factor2:
                            result.append(sorted((i+j)))
            return result
        return helper(2, n)


    #accepted.进一步简化上一方法。
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(start, n):
            result=[]
            for i in range(start, int(math.sqrt(n))+1):
                if n % i == 0:
                    factor2 = [[n/i]] + helper(i,n/i)
                    for j in factor2:
                            result.append([i]+j)
            return result
        return helper(2, n)


    #accepted
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(result, path, start, n):
            for i in range(start, int(math.sqrt(n))+1):
                if n % i == 0:
                    newPath = path+[i]
                    helper(result, newPath, i,n/i)
                    newPath += [n/i]
                    result.append(newPath)
        result =[]
        path=[]
        helper(result, path, 2, n)
        return result

sol = Solution()
print sol.getFactors(12)


"""
c++ solution:
class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;
        if (n==1) 
            return res;
        vector<int> path;
        helper(res, path, 2, n);
        return res;
    }
    #accepted
    void helper(vector<vector<int>> &res, vector<int> &path, int start, int n)
    {
        for (int i=start; i<=sqrt(n); i++)
       {    printf( "%d\n", i);
            if(n%i==0)
            {
                vector<int> newPath = path;
                newPath.push_back(i);
                helper(res, newPath,  i, n/i);
                newPath.push_back(n/i);
                res.push_back(newPath);
            }
        }
    }
    #accepted
    void helper(vector<vector<int>> &res, vector<int> &path, int start, int n)
    {
        for (int i=start; i<=sqrt(n); i++)
       { 
            if(n%i==0)
            {
                path.push_back(i);
                helper(res, path,  i, n/i);
                path.push_back(n/i);
                res.push_back(path);  
                path.pop_back();
                path.pop_back();
            }
        }
    }
};


"""
