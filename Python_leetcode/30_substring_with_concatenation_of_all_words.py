import collections
import copy

class Solution(object):
    #time limit exceeded
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        table = collections.defaultdict(int)
        for w in words:
            table[w] += 1
        wordlength = len(words[0])
        result = []
        numOfWords = len(words)
        for i in range(len(s)-wordlength*numOfWords+1):
            tableCopy = copy.deepcopy(table)
            count = 0
            k = i
            key = s[k:k+wordlength]
            while tableCopy[key] > 0 and count < numOfWords:
                tableCopy[key] -= 1
                count += 1
                k = k+wordlength
                if k >= len(s) - wordlength + 1: break
                key = s[k:k+wordlength]
            if count == 0:
                result.append(i)
        return result

     #pass
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        table = collections.defaultdict(int)
        for w in words:
            table[w] += 1
        wordlength = len(words[0])
        result = []
        numOfWords = len(words)
        for i in range(len(s)-wordlength*numOfWords+1):
            countTable = collections.defaultdict(int)
            count = 0
            k = i
            key = s[k:k+wordlength]
            while countTable[key] < table[key] and count < numOfWords:
                countTable[key] += 1
                count += 1
                k = k+wordlength
                key = s[k:k+wordlength]
            if count == numOfWords:
                result.append(i)
        return result

s="pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
words=["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]

s="helloworldtrymeworldhelloalthoughImokayworldtryhellome"
words=['hello','world','tryme']
sol = Solution()
print sol.findSubstring(s, words)
