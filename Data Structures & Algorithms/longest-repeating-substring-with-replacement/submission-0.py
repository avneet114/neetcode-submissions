"""
Understand - longest repeating character replacement
input - string s consisting of only uppercase english chars, integer k
we can choose up to k chars of the string and replace them with any other uppercase english char
output - length of the longest substring which contains only one distinct char
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)): #right pointer is gonna go thru every single item in string
            count[s[r]] = 1 + count.get(s[r], 0) #add 1 to current count, if ntg add default value 0
                
            while (r-l+1) - max(count.values()) > k: # window length - count of most frequent char > k
                count[s[l]] -= 1 #decrement the window is it's more than k
                l += 1 #move left pointer
            res = max(res, r-l+1) #size of window
        return res