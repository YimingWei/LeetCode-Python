# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1.迭代
        # pre, cur = None, head
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp       
        # return pre
        # 2.递归
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
