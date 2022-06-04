class Solution:
    # single pass
    def canPermutePalindrome(self, s: str) -> bool:
        count = collections.defaultdict(int)
        odd = 0
        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                odd -= 1
            else:
                odd += 1
        return odd <= 1

# using set
public class Solution {
    public boolean canPermutePalindrome(String s) {
        Set < Character > set = new HashSet < > ();
        for (int i = 0; i < s.length(); i++) {
            if (!set.add(s.charAt(i)))
                set.remove(s.charAt(i));
        }
        return set.size() <= 1;
    }
}

