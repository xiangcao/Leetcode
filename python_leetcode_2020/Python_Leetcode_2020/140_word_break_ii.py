class Solution:
    # Top Down - Memoization
    # dfs(word)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = collections.defaultdict(list)
        visited = set()
        def dfs(word):
            if word == "":
                return [[]]
            if word in memo:
                return memo[word]
            if word in visited:
                return [[]]
            for endIndex in range(1, len(word)+1):
                prefix = word[:endIndex]
                if prefix in wordSet:
                    for subsequence in dfs(word[endIndex:]):
                        memo[word].append([prefix] + subsequence)
            visited.add(word)
            return memo[word]
        dfs(s)
        return [" ".join(words) for words in memo[s]]

    # Bottom Up  - DP
    def wordBreak_3(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        dp = [[] for i in range((len(s)+1))]
        dp[0] = [""]
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []

        for i in range(1, len(s)+1):
            for j in range(i):
                postfix = s[j:i]
                if postfix in wordSet:
                    for prefix in dp[j]:
                        if prefix:
                            dp[i].append(prefix + " " + postfix)
                        else:
                            dp[i].append(postfix)
        return dp[-1]
