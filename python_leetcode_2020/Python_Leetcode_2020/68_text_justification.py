"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
"""

My solution
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        result= []
        while i < len(words):
            j = i + 1
            length = len(words[i])
            while j < len(words):
                if length + 1 + len(words[j]) <= maxWidth:
                    length += 1 + len(words[j])
                    j += 1
                else:
                    break
            count = (j-i-1)
            line = []
            # single word line or last line
            if count == 0 or j == len(words):
                for k in range(i, j):
                    line.append(words[k])
                    if k == j -1:
                        break
                    line.append(" ")
                line.append(" " * (maxWidth - length))
            else:
                spaces =  1 + (maxWidth - length) // count
                extra_spaces = (maxWidth - length) % count
                for k in range(i, j):
                    line.append(words[k])
                    if k == j - 1: #no space after last word in a line
                        break
                    line.append(" "*(spaces + (0 if extra_spaces <=0 else 1)))
                    extra_spaces -= 1
                
            i = j
            result.append("".join(line))
        return result


def fullJustify(self, words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]
How does it work? Well in the question statement, the sentence "Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right" was just a really long and awkward way to say round robin. The following line implements the round robin logic:

for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
What does this line do? Once you determine that there are only k words that can fit on a given line, you know what the total length of those words is num_of_letters. Then the rest are spaces, and there are (maxWidth - num_of_letters) of spaces. The "or 1" part is for dealing with the edge case len(cur) == 1.

The following is my older solution for reference, longer and less clear. The idea is the same, but I did not figure out the nice way to distribute the space at the time.

def fullJustify(self, words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            if len(cur) == 1:
                res.append( cur[0] + ' '*(maxWidth - num_of_letters) )
            else:
                num_spaces = maxWidth - num_of_letters
                space_between_words, num_extra_spaces = divmod( num_spaces, len(cur)-1)
                for i in range(num_extra_spaces):
                    cur[i] += ' '
                res.append( (' '*space_between_words).join(cur) )
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    res.append( ' '.join(cur) + ' '*(maxWidth - num_of_letters - len(cur) + 1) )
    return res
