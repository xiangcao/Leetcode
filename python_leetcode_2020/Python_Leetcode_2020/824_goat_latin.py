"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150
"""

class Solution(object):
    """
    Explanation
        Build a vowel set.(optional)
        Split 'S' to words.
        For each word, check if it starts with a vowel. (O(1) complexity with set).
        If it does, keep going. If it does not, rotate the first letter to the end.
        Add it to result string.
    """
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        def transform(w, i):
            if w[0] not in vowels:
                w = w[1:] + w[0]
            return w + 'ma' + 'a' * (i + 1)
        
        return " ".join(transform(w, i) for i, w in enumerate(S.split()))
