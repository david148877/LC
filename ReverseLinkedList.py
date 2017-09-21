# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        if not head.next: 
            return head
        
        previous = None
        current = head
        preceding = head.next
        
        while preceding:
            current.next = previous
            previous = current
            current = preceding
            preceding = preceding.next
            
        current.next = previous
        head = current
        
        return head
