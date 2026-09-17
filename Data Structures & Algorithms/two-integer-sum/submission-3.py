"""
Understand: 
Input: an array of integers nums and an integer target
Output: a list of indices i and j such that nums[i] nums[j] == target and i != j
Assumtpion: every input has exactly one pair of indices that satisfy the condition
Constraints: 2 <= nums.length <= 1000
-10,000,000 <=nums[i] <=10,000,000
-10,000,000 <= target <= 10,000,000
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #empty hashmap (dict) with val -> index

        for i, n in enumerate(nums): # walk thru nums, getting value n and i index
            diff = target - n
            # n1 + n2 = target 
            #target - n1 = n2 -> have i already seen this number that would complete this pair
            if diff in prevMap:
                return [prevMap[diff], i] # if it's alr in hashmap
            prevMap[n] = i
