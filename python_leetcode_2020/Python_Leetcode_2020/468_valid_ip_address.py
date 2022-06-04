class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.validIPV6(IP):
            return "IPv6"
        elif self.validIPV4(IP):
            return "IPv4"
        else:
            return "Neither"

    def validIPV6(self, IP: str) -> str:
        groups = IP.split(":")
        if len(groups) != 8: 
            return False
        def isValidIPV6Group(group):
            length = len(group)
            if length == 0 or length > 4:
                return False
            for c in group:
                if c.isdigit() or c in 'abcdefABCDEF':
                    continue
                else:
                    return False
            return True           
            
        for group in groups:
            if not isValidIPV6Group(group):
                return False
        return True
    
    def validIPV4(self, IP:str) -> str:
        groups = IP.split(".")
        if len(groups) != 4:
            return False
        def isValidIPV4Group(group):
            if (len(group)> 1 and group[0] == '0') or len(group) == 0:
                return False
            for c in group:
                if not c.isdigit():
                    return False
            value = int(group)
            if value > 255 or value < 0:
                return False
            return True
            
        for group in groups:
            if not isValidIPV4Group(group):
                return False
        return True
    
    # "20EE:FGb8:85a3:0:0:8A2E:0370:7334" 
    # Expected "Neither"

    #"f:f:f:f:f:f:f:f"
    # Expected  "IPv6"


Better solution from leetcode

def validIPAddress(self, IP):
        def isIPv4(s):
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False
            
        def isIPv6(s):
            if len(s) > 4: return False
            try: return int(s, 16) >= 0 and s[0] != '-'
            except: return False

        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")): 
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")): 
            return "IPv6"
        return "Neither"
    # Expected  "IPv6"
