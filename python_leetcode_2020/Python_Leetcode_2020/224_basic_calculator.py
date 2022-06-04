class Solution:
    Stack<Integer> stack = new Stack<Integer>();
    int result = 0;
    int number = 0;
    int sign = 1;
    for(int i = 0; i < s.length(); i++){
        char c = s.charAt(i);
        if(Character.isDigit(c)){
            number = 10 * number + (int)(c - '0');
        }else if(c == '+'){
            result += sign * number;
            number = 0;
            sign = 1;
        }else if(c == '-'){
            result += sign * number;
            number = 0;
            sign = -1;
        }else if(c == '('){
            //we push the result first, then sign;
            stack.push(result);
            stack.push(sign);
            //reset the sign and result for the value in the parenthesis
            sign = 1;   
            result = 0;
        }else if(c == ')'){
            result += sign * number;  
            number = 0;
            result *= stack.pop();    //stack.pop() is the sign before the parenthesis
            result += stack.pop();   //stack.pop() now is the result calculated before the parenthesis
            
        }
    }
    if(number != 0) result += sign * number;
    return result;

  # stack: stores the context sign
  # 
  def calculate(self, s):
    res, num, sign, stack = 0, 0, 1, [1]
    for i in s+"+":
	if i.isdigit():
	    num = 10*num + int(i)
	elif i in "+-":
	    res += num * sign * stack[-1]
	    sign = 1 if i=="+" else -1
	    num = 0
	elif i == "(":
	    stack.append(sign * stack[-1])
	    sign = 1
	elif i == ")":
	    res += num * sign * stack[-1]
	    num = 0
	    stack.pop()
    return res

/*Java solution similar to 2nd solution above
Principle:

(Sign before '+'/'-') = (This context sign);
(Sign after '+'/'-') = (This context sign) * (1 or -1);
Algorithm:

Start from +1 sign and scan s from left to right;
if c == digit: This number = Last digit * 10 + This digit;
if c == '+': Add num to result before this sign; This sign = Last context sign * 1; clear num;
if c == '-': Add num to result before this sign; This sign = Last context sign * -1; clear num;
if c == '(': Push this context sign to stack;
if c == ')': Pop this context and we come back to last context;
Add the last num. This is because we only add number after '+' / '-'.
*/
public int calculate(String s) {
    if(s == null) return 0;
        
    int result = 0;
    int sign = 1;
    int num = 0;
            
    Stack<Integer> stack = new Stack<Integer>();
    stack.push(sign);
            
    for(int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
                
        if(c >= '0' && c <= '9') {
            num = num * 10 + (c - '0');
                    
        } else if(c == '+' || c == '-') {
            result += sign * num;
            sign = stack.peek() * (c == '+' ? 1: -1); 
            num = 0;
                    
        } else if(c == '(') {
            stack.push(sign);
                    
        } else if(c == ')') {
            stack.pop();
        }
    }
            
    result += sign * num;
    return result;
} 
  # my own messy solution 
  def calculate(self, s: str) -> int:
        stack = []
        hasnumber, operand = False, 0
        for c in s:
            if c.isdigit():
                operand = operand * 10 + int(c)
                hasnumber = True
                continue
            else:
                if hasnumber:
                    stack.append(operand)
                    hasnumber, operand = False, 0
            if c in '+-(':
                stack.append(c)
            elif c == ')':
                operand = 0
                sum = 0
                while stack:
                    e = stack.pop()
                    if e == '(':
                        stack.append(sum + operand)
                        operand = 0
                        break
                    elif e == '-':
                        sum += -operand
                        operand = 0
                    elif e == '+':
                        sum += operand
                        operand = 0
                    else:
                        operand = e
        sum = 0        
        while stack:
            e = stack.pop()
            if e == '-':
                sum += -operand
                operand = 0
            elif e == '+':
                sum += operand
                operand = 0 
            else:
                operand = e
            
        return sum + operand
        
                
                    
            
