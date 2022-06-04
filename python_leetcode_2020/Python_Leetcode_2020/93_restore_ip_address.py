"""
Given a string s containing only digits. Return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single points and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result=[]
        def dfs(count, idx, path):
            if idx == len(s) or count == 4:
                if idx == len(s) and count == 4:
                    result.append(path)
                return
            for i in range(3):
                if idx + i + 1 > len(s):
                    break
                segment = s[idx:idx+i+1]
                if segment[0] == '0' and len(segment) >1 :
                    break
                if len(segment) == 3 and int(segment) > 255:
                    break
                if path:
                    dfs(count+1, idx+i+1, path + "." + segment)
                else:
                    dfs(count+1, idx+i+1, segment)
                
        dfs(0, 0, "")
        return result
