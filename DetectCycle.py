# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1.哈希表 O(n)
        # d = {}
        # while head:
        #     if d.get(head):
        #         return head
        #     else:
        #         d[head] = 1
        #         head = head.next
        # 2.快慢指针
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return None
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        slow = head
        while slow != fast:
            fast, slow = fast.next, slow.next
        return fast
