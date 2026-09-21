"""
Understanding: Longest Substring Without Repeating Characters
Input: a string s
Output: length of the longest substring without duplicate chars
a substring a contiguous sequence of characters within a string
Match: sliding window technique
Plan:
- keep one window that always has unique characters. expand it by moving the right pointer
- if we ever see a repeated character, we shrink the window from the left until duplicate is removed
- track max size - to count how many integers are in a range from a to b inclusive, it's b - a + 1
Implement:
Review
Evaluate: time - O(N) and space - O(m) where n is the length of the string and m is the total number of unique chars in string
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        