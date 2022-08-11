class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            # dict里面的每个value都是list
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())
