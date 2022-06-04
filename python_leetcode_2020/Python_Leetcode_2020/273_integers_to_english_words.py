class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)
        
        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen',
            }
            return switcher.get(num)
        
        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety',
            }
            return switcher.get(num)
        
        def two(num):
            if not num:
                return ""
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                ten_order = num//10
                remainer = num % 10
                return ten(ten_order) + ' ' + one(remainer) if remainer else ten(ten_order)
            
        def three(num):
            hundred = num //100
            remainder = num % 100
            if hundred and remainder:
                return one(hundred) + " Hundred " + two(remainder)
            elif hundred and not remainder:
                return one(hundred) + " Hundred"
            elif not hundred and remainder:
                return two(remainder)
            return ""
        billion = num // 1000000000
        billion_remainder = (num % 1000000000)
        million = billion_remainder // 1000000
        million_remainder = billion_remainder % 1000000
        thousand = million_remainder //1000
        thousand_remainder = million_remainder % 1000
        
        if not num:
            return 'Zero'
        result = ''
        if billion:
            result += three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if thousand_remainder:
            result += ' ' if result else ''
            result += three(thousand_remainder)
        return result
        



# removed the `if else` 
class Solution:
    def numberToWords(self, num: int) -> str:   
        def three(num):
            hundred = num // 100
            remainder = num % 100
            result = []
            if hundred:
                result.append(one(hundred) + " Hundred")
            if remainder:
                result.append(two(remainder))
            return ' '.join(result)
        
        def one(num):
            mapping = {1: 'One', 
                       2: 'Two',
                       3: 'Three',
                       4: 'Four',
                       5: 'Five',
                       6: 'Six',
                       7: 'Seven',
                       8: 'Eight',
                       9: 'Nine',}
            return mapping[num]
    
        def ten(num):
            mapping = {2: 'Twenty',
                      3: 'Thirty',
                      4: 'Forty',
                      5: 'Fifty',
                      6: 'Sixty',
                      7: 'Seventy',
                      8: 'Eighty',
                      9: 'Ninety'}
            return mapping[num]
       
        def two_less_20(num):
            mapping = {10: 'Ten',
                       11: 'Eleven',
                       12: 'Twelve',
                       13: 'Thirteen',
                       14: 'Fourteen',
                       15: 'Fifteen',
                       16: 'Sixteen',
                       17: 'Seventeen',
                       18: 'Eighteen',
                       19: 'Nineteen'                
            }
            return mapping[num]
        
        def two(num):
            if num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                ten_order = num // 10
                ten_remainder = num % 10
                result = ten(ten_order)
                if ten_remainder:
                    result += ' ' + one(ten_remainder)
                return result

        billion = num // 1000000000
        billion_remainder = num % 1000000000
        million = billion_remainder // 1000000
        million_remainder = billion_remainder % 1000000
        thousand = million_remainder // 1000
        thousand_remainder = million_remainder % 1000
        
        if not num:
            return 'Zero'
        result = []
        if billion:
            result.append(three(billion) + ' Billion')
        if million:
            result.append(three(million) + ' Million')
        if thousand:
            result.append(three(thousand) + ' Thousand')
        if thousand_remainder:
            result.append(three(thousand_remainder))

        
        return ' '.join(result)
     
