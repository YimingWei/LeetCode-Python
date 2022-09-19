# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next
        return stack == stack[::-1]
