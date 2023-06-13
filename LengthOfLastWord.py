class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pure_s = s.strip(" ")
        i = len(pure_s) - 1
        count = 0
        while i >= 0 and pure_s[i] != " ":
            count += 1
            i -= 1
        return count
