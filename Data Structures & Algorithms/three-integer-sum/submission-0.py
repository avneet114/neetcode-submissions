"""
Unsing uMPIRE method:
Understand:
Input - nums : list[int]
Output - triplets whose sum = 0 (nums[i] + nums[j] + nums[k] == 0)
Constraints:
- i,j,k are distinct
- no duplicate triplets
- order doesn't matter
- reuse items?
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        res = []
        nums.sort() # sort first so we can use two pointers (like twoSum2) AND so duplicate values sit next to each other, making them easy to skip
        # a is fixed number

        for i, a in enumerate(nums): # walk thru each number, fixing one at a time as the "first" number of the triplet
            if a > 0: # since sorted ascending, if the fixed number is already positive, the two numbers after it (>= a, so also positive) can never bring the sum back down to 0
                break # no point checking the rest of the array -> stop early

            if i > 0 and a == nums[i-1]: # skip repeats of the same fixed number so we don't reprocess (and re-append) triplets starting with a value we already fully explored
                continue

            l, r = i+1, len(nums) -1 # two pointers over the REST of the array (after i) -> l starts right after a, r starts at the very end
            while l<r: # same shrinking-window pattern as twoSum2, just searching for nums[l]+nums[r] == -a instead of a fixed target
                threeSum = a + nums[l] + nums[r] # candidate triplet sum
                if threeSum > 0: # sum too big -> need a smaller number -> shrink from the right (largest value)
                    r-=1
                elif threeSum < 0: # sum too small -> need a bigger number -> grow from the left (smallest value)
                    l += 1
                else: # a + nums[l] + nums[r] == 0 -> found a valid triplet
                    res.append([a, nums[l], nums[r]])
                    l +=1 # move both pointers inward to look for more triplets with this same a
                    r -= 1
                    while nums[l] == nums[l-1] and l<r: # skip duplicate values for l so we don't add the same triplet again
                        l+=1 # since l always moves at least once after a match, this guarantees the next match (if any) uses a genuinely new l value -> no duplicate triplets, even though we never explicitly skip duplicates on r
        return res