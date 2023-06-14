class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = list(zip(*strs))
        res = ""
        for i in range(len(s)):
            if len(set(s[i])) == 1:
                res += s[i][0]
            else:
                break
        return res
