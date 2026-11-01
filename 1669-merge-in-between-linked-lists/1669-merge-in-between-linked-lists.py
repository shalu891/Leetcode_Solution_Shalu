# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next
            
        curr_b = prev_a
        for _ in range((b - a) + 2):
            curr_b = curr_b.next
            
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
            
        prev_a.next = list2
        tail2.next = curr_b
        
        return list1

        