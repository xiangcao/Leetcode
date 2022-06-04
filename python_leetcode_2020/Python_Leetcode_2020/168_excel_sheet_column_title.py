class Solution:
    def convertToTitle(self, n: int) -> str:
        num = n
        return "" if num == 0 else (self.convertToTitle((num - 1) // 26) + chr((num - 1) % 26 + ord('A')))
