# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 递归终止条件
        if not head or not head.next:
            return head
        # （1）找中点，切断
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid, slow.next = slow.next, None #mid作为另一半的头节点
        # （2）左右两边，重新组合
        left = self.sortList(head)
        right = self.sortList(mid)
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: #左边值小则取左边，并将指针移一位
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right #while循环结束必有left或者right还有剩余节点，将h下一节点指针指向它，连接剩余节点
        return res.next
