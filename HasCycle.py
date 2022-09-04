# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # 1.计数 O(1)
        # count = 0
        # while head and count<= 10000: #因为节点数最多10000个
        #     count += 1
        #     head = head.next
        # return count > 10000
        # # 2.哈希表 O(n)
        # h = {}
        # while head:
        #     if h.get(head):
        #         return True
        #     h[head] = 1
        #     head = head.next
        # return False
        # 3.将val标记为特殊值 O(1)
        while head:
            if head.val == 'modified':
                return True
            head.val = 'modified'
            head = head.next
        return False
