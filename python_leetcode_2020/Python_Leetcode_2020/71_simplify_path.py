"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        skip = set(["..", ".",""])

        for dir in path.split("/"):
            if dir == ".." and stack:
                stack.pop()
            elif not dir in skip:
                stack.append(dir)
        res = "/" + "/".join(stack)
        #res = ""
        #for dir in stack:
        #    res = res + "/" + dir
        return "/" if not res else res
