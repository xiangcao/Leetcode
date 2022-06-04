"""
We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.
"""
class Solution:
    """
    Approach 1: Optimized Exhaustive Search


"""
    def minStickers1(self, stickers: List[str], target: str) -> int:
        t_count = collections.Counter(target)
        """
        Firstly, for each sticker, let's create a count of that sticker (a mapping letter -> sticker.count(letter)) that does not consider letters not in the target word. Let A be an array of these counts. Also, let's create t_count, a count of our target word."""
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        # remove all sticker that are dominated by other stickers
        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        self.best = len(target) + 1
        def search(ans = 0):
            if ans >= self.best: return
            if not A:
                if all(t_count[letter] <= 0 for letter in t_count):
                    self.best = ans
                return

            sticker = A.pop()
            used = max((t_count[letter] - 1) // sticker[letter] + 1
                        for letter in sticker)
            used = max(used, 0)

            for letter in sticker:
                t_count[c] -= used * sticker[letter]

            search(ans + used)
            for i in range(used - 1, -1, -1):
                for letter in sticker:
                    t_count[letter] += sticker[letter]
                search(ans + i)

            A.append(sticker)

        search()
        return self.best if self.best <= len(target) else -1
    
    def minStickers(self, stickers, target):
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        stickers = ["".join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in range(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]



