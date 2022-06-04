"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for string in strings:
            code=[]
            for i in range(len(string)-1):
                diff = ord(string[i+1]) - ord(string[i])
                if diff < 0: diff += ord('z') - ord('a') + 1
                code.append(str(diff))
            groups["_".join(code)].append(string)
        return groups.values()
            

# 2nd round
    # this is buggy version; would fail for test case ["abm", "bmn"]; both encoded to 111, but they belong to different group
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapping = collections.defaultdict(list)
        for string in strings:
            encoding = []
            for i in range(1, len(string)):
                offset = (ord(string[i]) - ord(string[i-1])) % 26
                encoding.append(str(offset))
            mapping[''.join(encoding)].append(string)
        return mapping.values()

    # this is fixed version
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapping = collections.defaultdict(list)
        for string in strings:
            encoding = []
            for i in range(1, len(string)):
                offset = (ord(string[i]) - ord(string[i-1])) % 26
                encoding.append(str(offset))
            mapping['_'.join(encoding)].append(string)
        return mapping.values()
