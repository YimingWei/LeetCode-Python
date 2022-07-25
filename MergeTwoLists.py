# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 1.递归法
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

        # 2. 迭代法
        # prehead = ListNode(-1)
        # pre = prehead
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         pre.next = list1
        #         list1 = list1.next
        #     else:
        #         pre.next = list2
        #         list2 = list2.next
        #     pre = pre.next
        # if list1 is not None:
        #     pre.next = list1
        # else:
        #     pre.next = list2
        # return prehead.next
