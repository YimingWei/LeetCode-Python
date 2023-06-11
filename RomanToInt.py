class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000, 
                    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        res = 0
        i = 0
        while i<len(s):
            if hash_map.get(s[i:i+2]):
                res += hash_map.get(s[i:i+2])
                i += 2
            else:
                res += hash_map.get(s[i])
                i += 1
        return res
