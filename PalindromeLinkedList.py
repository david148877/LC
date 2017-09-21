'''
For linked list 1->2->3->2->1, the code below first makes the list to be 1->2->3->2<-1 and the second 2->None, then make 3->None, for even number linked list: 1->2->2->1, make first 1->2->2<-1 and then the second 2->None, and lastly do not forget to make the first 2->None 
(If forget it still works while the idea behind is a little bit different).

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head:
            return True
        
        #find mid node
        fast = slow = head
        
        while fast.next and fast.next.next:   #set up fast speeds is twice to slow
            slow = slow.next
            fast = fast.next.next
        #reverse second half
        p = slow.next 
        last = None    
        slow.next = None        #not needed, but clearer
        '''
        last is before the second half
        (a none insert into the beginning of the second half )     
        1->2->3->4->5->6->7  => none->5->6->7
        then we can reverse the second half like reverse linked list problem
        '''
        
        '''
        <Stephen>
        def reverseLinkedListIterative(self, head):
            if not head or not head.next: return None
            preCurrent = None
            currentNode = head
            while currentNode:
                nextNode = currentNode.next
                currentNode.next = preCurrent
                preCurrent = currentNode
                currentNode = nextNode
            return preCurrent

        '''
        while p:               #p equals to currentNode above
            next = p.next
            p.next = last
            last = p           #last equals to preCurrent above 
            p = next
        #check palindrome
        p1 = last
        p2 = head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
            
        '''
        <Stephen>
        #check palindrome
        p1, p2 = last, head
        while p1 :
            if not (p1.val == p2.val): return False
            p1, p2 = p1.next, p2.next
        return True

        '''
        
        
        #resume linked list(optional)
        p, last = last, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        slow.next = last
        return p1 is None

