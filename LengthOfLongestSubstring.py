class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, res = 0, 0, 0
        windows = {}
        n = len(s)
        while right in range(n):
            cur = s[right]
            right += 1
            if cur not in windows:
                windows[cur] = 1
            else:
                windows[cur] += 1
            while windows[cur] > 1:
                delete = s[left]
                left += 1
                windows[delete] -= 1
            res = max(res, right - left)
        return res
