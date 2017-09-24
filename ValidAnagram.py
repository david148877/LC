class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #use Python lib, collections.Counter  ref: https://docs.python.org/2/library/collections.html#collections.Counter
        from collections import Counter
        return Counter(s).items() == Counter(t).items()    #either True or False   #c.items()      convert c to a list of (element, counts) pairs
        
        
