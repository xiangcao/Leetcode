class Solution:
    # brute force:
    # 1000000000
    # time limit exceeded
    def findNthDigit(self, n: int) -> int:
        i = 1  
        while True:
            n -= len(str(i))
            if n <= 0:
                break
            i += 1
        return int(str(i)[n-1])
    
    #PASS 28ms; 80% faster
    def findNthDigit(self, n: int) -> int:
        start = 1
        count = 9
        length = 1
        
        while n > count * length:
            n -= count * length
            count *= 10
            length += 1
            start *= 10
        start += (n-1)/length
        return int(str(start)[(n-1)%length])
             
