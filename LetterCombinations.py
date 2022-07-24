class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # 1.回溯法
        # def backstrace(combination, nextdigit):
        #     if len(nextdigit) == 0:
        #         res.append(combination)
        #     else:
        #         for letter in phone[nextdigit[0]]:
        #             backstrace(combination + letter, nextdigit[1:])
        
        # res = []
        # combination = ''
        # backstrace(combination, digits)
        # return res

        # 2.队列法
        res = ['']
        for i in digits:
            length = len(res)
            for n in range(length):
                temp = res.pop(0)
                for j in phone[i]:
                    res.append(temp+j)
        return res
