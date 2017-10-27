import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        head = ListNode(0)
        pre = head
        carry = 0
        while (l1 and l2):
            sum = ( l1.val + l2.val + carry )
            result = sum % 10
            carry = int( sum / 10)
            head.next = ListNode(result)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        if l2: l1 = l2
        head.next = l1
        while head.next:
            sum = ( head.next.val + carry )
            head.next.val = sum % 10
            carry = int (sum/10)
            head = head.next
        if carry:
            head.next = ListNode(carry)
        return pre.next

sol = Solution()
l1 = ListNode(1)
l2 = construct_node_from_list([9,9])

print sol.addTwoNumbers(l1,l2)

