"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

"""

class Codec:

    def encode(self, strs):
        return ''.join(s.replace('|', '||') + ' | ' for s in strs)
    
    def decode(self, s):
        return [t.replace('||', '|') for t in s.split(' | ')[:-1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))



class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return None
        result = ""
        for str in strs:
            lengthstr = [chr(0)]*4
            length = len(str)
            byte = 4
            while length:
               lengthstr[byte-1] = chr(length %256)
               byte -= 1
               length /= 256
            prefix = "".join(lengthstr)
            result += prefix + str.encode("utf-8")
        return result

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if s is None:
            return []
        result=[]
        totallength = len(s)
        if totallength == 0:
            return [""]
        i = 0 
        def convertStrToInt_256Base(prefixlen):
            sum = 0
            for i in prefixlen:
                sum = sum * 256 + ord(i)
            return sum
        while i < totallength:
            prefixlen = s[i:i+4]
            length = convertStrToInt_256Base(prefixlen)
            result.append(s[i+4:i+length+4])
            i = i + length + 4
        return result
            
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
