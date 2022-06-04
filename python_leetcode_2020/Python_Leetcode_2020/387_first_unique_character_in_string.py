"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.
"""
class Solution {
public:
    int firstUniqChar(string s) {
        vector<pair<int, int>>v(26); // {x,y} , x means count of a char, and y means the index at which the char was first found
        for(int i = 0; i < s.size(); ++i){
            char c = s[i];
            if(v[c-'a'].first == 0){
                v[c-'a'].second = i;
            }
            v[c-'a'].first = v[c-'a'].first + 1;
        }

        int minIndex = INT_MAX;
        for(auto i: v){
            if(i.first == 1){
                minIndex = min(minIndex, i.second);
            }
        }
        return minIndex == INT_MAX ? -1 : minIndex;
    }
};
