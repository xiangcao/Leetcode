class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping=['', '','abc','def','ghi','jkl','mno','pqrs', 'tuv', 'wxyz']
        result = []
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        #acc: List[str]
        #当已经获得digits[0:i-1]的所有letter combinations以后，加入digits[i]后新combinations为加入每个可能对应的字母加到之前的解集中。这里需要克隆多份之前的解集。
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])


#c++ solution : http://bangbingsyb.blogspot.com/2014/11/leetcode-letter-combinations-of-phone.html
#python http://2hwp.com/LeetCode/17%20Letter%20Combinations%20of%20a%20Phone%20Number/
#python 2 http://www.cnblogs.com/zuoyuan/p/3779761.html  (function closure, avoid some parameter passing)
