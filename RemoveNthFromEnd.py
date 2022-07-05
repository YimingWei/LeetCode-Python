# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建一个虚拟的头指针
        pre_head = ListNode(next=head)
        # 定义快慢指针
        pre = pre_head
        post = head
        # 快指针先行n-1
        for i in range(n):
            post = post.next
        # 快慢指针同时遍历，快指针到结尾，慢指针到倒数第n+1个结点
        while post != None:
            pre = pre.next
            post = post.next
        # 跳过倒数第n个结点
        pre.next = pre.next.next
        return pre_head.next
