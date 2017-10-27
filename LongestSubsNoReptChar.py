import sys
sys.path.append("/Users/jinzhao/leetcode/")
class Solution(object):
    """
       Constant space complexity, since there are only constant amount of char so the 
       hash table is only constant size
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        front_ptr = 0
        back_ptr = 0
        position_dict = {} 
        max_len = 0
        while front_ptr < len(s):
            if s[front_ptr] in position_dict and position_dict[s[front_ptr]] >= back_ptr:
               back_ptr = position_dict[s[front_ptr]] + 1
            else:
               max_len = max( max_len, (front_ptr - back_ptr + 1) )
            position_dict[s[front_ptr]] = front_ptr
            front_ptr  = front_ptr + 1
        return max_len

    def lengthOfLongestSubstring_simple (self, s):
        """
        :type s: str
        :rtype: int
        """
        back_ptr = 0
        position_dict = {}
        max_len = 0
        for i in xrange(0, len(s)):
            #Remember this condition ! (Second half)
            if s[i] in position_dict and position_dict[s[i]] >= back_ptr:
               back_ptr = position_dict[s[i]] + 1
            else:
               max_len = max( max_len, (i - back_ptr + 1) )
            position_dict[s[i]] = i
        return max_len
#test 
if  __name__ == "__main__":
    sol = Solution()
    print sol.lengthOfLongestSubstring("abcabcbb")
    print sol.lengthOfLongestSubstring("dvdf")
    print sol.lengthOfLongestSubstring("abba")
    print sol.lengthOfLongestSubstring("tmmzuxt")
