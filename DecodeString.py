class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == "[":
                stack.append([multi, res]) #将当前的multi和res先入栈保存
                multi, res = 0, "" #重置multi和res，作为新一层"[]"的开始
            elif c == "]":
                cur_multi, cur_res = stack.pop() #将之前存到栈内的值pop出来
                res = cur_res + cur_multi * res
            elif "0" <= c <= "9":
                multi = multi * 10 + int(c) #c为数字，则根据十进制计算multi
            else:
                res += c #c为字符则接到res后边
        return res
