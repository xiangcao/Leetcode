class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        #1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, 31131211131221, 13211311123113112211, 11131221133112132113212221
        number= '1'
        def count(number):
            '''
            :type number: str
            :rtype: str
            '''
            count = 1 
            say=''
            for i in range(1,len(number)):
                if number[i] == number[i-1]:
                    count += 1
                else:
                    say += str(count) + number[i-1]
                    count = 1
            say += str(count) + number[-1]
            return say
        for i in range(1, n):
            number = count(number)
        return number
