"""
Understand - permutation in string
input: two strings s1 and s2
output - boolean (true if s2 contains a permutation of s1), false otherwise.
that means permutation of s1 exists as a substring of s2 -> return true
constraints:
- only lowercase letters
Match - sliding window approach 
Plan
- sliding window approach on s2 with fixed window size equal to length of s1
- track the current window -> we maintain a frequent count of chars in s2 and also for s1
- at each step, if frequency count matches of s1, we return true
- as we slide the window forward, we update counts by removing the left char and adding new right char
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26 #char fequency array for s1
        s2Count = [0] * 26 #first window of s2 of sixe len(s1)
        #it can only have 26 chars since we know it's all lowercase
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        #count how many positions match between the two arrays
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        #slide the window from to right across s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
        
        # at each step, add the new right char and update counts/matches
        # remove left char and update counts/matches
        # if matches == 26, return true
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

        # after loop, return whether matches == 26

        