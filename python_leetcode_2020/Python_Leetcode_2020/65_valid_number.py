"""
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
"""
class Solution(object):
    # 1E9 True
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [{"digit": 1, "sign":2, ".": 3, "blank": 0},
                 {"digit": 1, ".": 4 , "e": 5, "blank": 9},  #1, terminal
                 {"digit": 1, ".": 3}, #2
                 {"digit": 6},    #3
                 {"digit": 4, "e": 5, "blank": 9}, #4 terminal
                 {"digit": 7,  "sign": 8}, #5
                 {"digit": 6 , "e":5 , "blank": 9}, #6 terminal
                 {"digit": 7, "blank": 9},  #7 terminal state
                 {"digit": 7},  
                 {"blank": 9}  #9 terminal 
                ]
        current_state = 0
         
        for c in s:
                if c == ' ':
                    c = 'blank'
                elif c == '+' or c=='-':
                    c = 'sign'
                elif c >= '0' and c <= '9':
                    c = 'digit'
                elif c == 'E':
                    c = 'e'

                if c not in state[current_state].keys():
                    return False
                
                current_state = state[current_state][c]
        return current_state in [9, 7, 6, 4 ,1]
