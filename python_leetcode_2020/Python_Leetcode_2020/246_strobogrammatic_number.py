"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.
"""

def isStrobogrammatic(self, num):
    """
    :type num: str
    :rtype: bool
    """
    maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
    i,j = 0, len(num) - 1
    while i <= j:
        if (num[i], num[j]) not in maps:
            return False
        i += 1
        j -= 1
    return True
