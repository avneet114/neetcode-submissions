""" group anagrams
# Understand:
Lists and arrays are mutable and canot be used as dictionary keys directly so we must convert character frequency arrays  as keys to a tuple
Input - an array strings strs
Output - sublists of grouped anagrams
Constraints - strs[i] is made up of lowercase english letters = 26 count

Match - hashmap, dictionary
Plan 
- create a hashmap default dict where each key is a 26 length tuple representing char frquencies and each value if a list of strings belonging to that anagram group
- loop over each string in input
- initialize a count array of size 26 with all zeroes
- for each char c in string, increment the count at the corresponding indez
- convert count to tuple and use it as a key
- append the string to the list associated with this key
- after processing all strings, return all the lists stored in the hashmap

Implement:
Review:
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Evaluate:
Time - O(m*n) where m is number of strings and n is length of longest string
Space - O(m)
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) #mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # can use a fixed size array as letters are constrained to lowercase a-z -> bit faster/simpler

            for c in s:
                count[ord(c) - ord("a")] += 1 # ord() gives the ASCII code of a char. 
                # this converts any lowercase letter into a 0-25 index into count array
            
            res[tuple(count)].append(s) # THIS IS THE KEY : word
            # dictionary keys must be hashable (immutable). a lsit is mutable so python wont allow res[count] -> throws typeerror
            # a ty=uple is a immutable version of a list, same values, so tuple(count)
        
        return list(res.values())

    # key (as a tuple) is: (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
    # value "cat"