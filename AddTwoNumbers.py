# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry_flag=0) -> ListNode:
        n1, n2 = l1.val if l1 else 0, l2.val if l2 else 0
        s = n1 + n2 + carry_flag
        val, carry_flag = s % 10, 1 if s > 9 else 0
        next1, next2 = l1.next if l1 else None, l2.next if l2 else None
        if next1 or next2 or carry_flag:
            return ListNode(val, self.addTwoNumbers(next1, next2, carry_flag))
        return ListNode(val)
