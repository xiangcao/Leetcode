"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        stack = []
        i = 0
        while i < len(s):
            j = i
            # do not process '('
            if(s[i] == ')'):
                stack.pop()
            elif(s[i].isdigit() or s[i] == '-'):
                while(i + 1 < len(s) and s[i+1].isdigit()):
                    i += 1
                currentNode = TreeNode(int(s[j:i + 1]))
                if stack:
                    parent = stack[-1]
                    if(parent.left != None):
                        parent.right = currentNode
                    else:
                        parent.left = currentNode
                stack.append(currentNode)
            i += 1
        return stack[-1] if stack else None

private int index = 0;    
public TreeNode str2tree(String st) {
    if (index == st.length()) return null;                
    StringBuilder num = new StringBuilder(); //extract number
    while (index < st.length()) { 
        char c = st.charAt(index);
        if(c!='('&&c!=')') {
            num.append(c);
            index++; 
        } else break;
    }       
    TreeNode node = new TreeNode(Integer.parseInt(num.toString())); // create new node       
    if (index < st.length() && st.charAt(index) == '('){// check parenthesis type            
        index++;
        node.left = str2tree(st);// create left child node
        index++;            
        if (index < st.length() && st.charAt(index) == '('){                
            index++;
            node.right = str2tree(st);// create right child node
            index++;
        }
    }
    return node; // if meets ')', return to parent node
}
