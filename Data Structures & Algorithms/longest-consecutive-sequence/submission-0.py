"""
Using Umpire Method:
Understand: given an array of integers nums, return the lenngth of the longest consecutive sequence of elements that can be found.
consecutive sequence is a sequence of elements in which each element is eactly one greater than the previous element

example: 
nums = [2,20,4,10,3,4,5]
output = 4 -> 2,3,4,5
input - nums : list[int] 
output - len(long) -> length of longest consecutive sequence
constraints:
- the elements do NOT have to be consecutive in order in original array
- time complexity must be O(n)
- 0 <= nums.length <= 100,000
- 10^9 <= nums[i] <= 10^9

Edge cases:
- if the array is empty -> it should return 0
- if there are duplicates -> ignore (assumption)

Match: can store unique values in a hash set -> lookup is O(1). to find the beginning of sequence, num-1 shouldn't be in the set

Plan: 
- convert the list into a numSet for O(1) lookups
- initialize longest to track the length of longest consecutive sequence
for each num in numSet
- check if num-1 is not in the set
- if true, num is the start of the sequence
- initialize length = 1
- while num+length exists in the set, increase length
- update longest with the max length founf
return longest after scanning all numbers
Implement:
Review:
Evaluate: 
- Time: O(n) - despite the for + nested while, every number is only ever "walked" as part
  of the ONE chain it truly belongs to, since only true chain-starts trigger a walk.
  total while-loop steps across the whole run is bounded by n, not n^2.
- Space: O(n) - for storing numSet
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length +=1
                longest = max(length, longest)
        return longest
        