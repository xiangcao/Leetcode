class Solution(object):
    def restoreIpAddresses(self,s):
        # iterative solution
        result = []
        len_s = len(s)
         
        def check_valid(ipSegmentList):
            for ipsegment in ipSegmentList:
                if ipsegment[0] == '0' and ipsegment != '0':
                    return False
                if int(ipsegment) > 255:
                    return False
            return True
        for i in range(1,4):
            if len_s - i > 9 :
                continue
            for j in range(i+1, i+4):
                if len_s - j > 6:
                    continue
                for k in range(j+1, j+4):
                    if k >= len_s:
                        continue
                    if len_s - k > 3:
                        continue
                    ip_1 = s[:i]
                    ip_2 = s[i:j]
                    ip_3 = s[j:k]
                    ip_4 = s[k:]
                    ip = [ip_1, ip_2, ip_3, ip_4]
                    if check_valid(ip):
                        result.append(".".join(ip))
        return result
                     
    def restoreIpAddresses(self,s):
        #dfs solution
        
        def restoreIP(s, result, curIndex, curIP, count):
            if count>4:
                return
            if count == 4 and curIndex == len(s):
                result.append(curIP)
                return 
            for i in range(3):
                if (curIndex + i) >= len(s):
                    return
                segment = s[curIndex: curIndex+i+1]
                if segment.startswith("0") and len(segment)>1:
                    return
                if int(segment)>255:
                    return
                restoreIP(s, result, curIndex+i+1, curIP+segment+(".","")[count==3], count+1)
        result = []
        restoreIP(s, result, 0, "", 0)
        return result
                
