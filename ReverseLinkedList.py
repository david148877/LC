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
        previous = None
        current = first
        preceding = first.next
        
        if not head:
            return None
        if not head.next: 
            return head
        
        while preceding:
            current.next = previous
            previous = current
            current = preceding
            preceding = preceding.next
            
        current.next = previous
        first = current
        
        return first
        
       

    

    
