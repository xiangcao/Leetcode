"""
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

Example:

Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]


Note:

You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.
"""
# https://leetcode.com/problems/design-in-memory-file-system/solution/

from collections import defaultdict
class Node:
    def __init__(self):
        self.child=defaultdict(Node)
        self.content=""
        
class FileSystem(object):

    def __init__(self):
        self.root=Node()
        
    def find(self,path):#find and return node at path.
        curr=self.root
        if len(path)==1:
            return self.root
        for word in path.split("/")[1:]:
            curr=curr.child[word]
        return curr

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        curr=self.find(path)
        if curr.content:#file path,return file name
            return [path.split('/')[-1]]
        return sorted(curr.child.keys())
		
    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        self.find(path)

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        curr=self.find(filePath)
        curr.content+=content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        curr=self.find(filePath)
        return curr.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
