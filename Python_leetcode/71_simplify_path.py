class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        #how about "../file/" or "/file/.../dbc/", "/../", "/.."
        separated = path.split("/")
        result=[]
        for i in separated:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if len(result):
                    result.pop()
                if len(result):
                    result.pop()
            else:
                result.extend(["/",i])
        return ''.join(result) if result else "/"
