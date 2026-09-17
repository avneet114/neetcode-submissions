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
        A = []
        for i, num in enumerate(nums):
            A.append([num, i]) #A[i] -> [num, i]
        
        A.sort()
        #two pointer
        i, j = 0, len(nums) - 1
        while i<j:
            cur = A[i][0] + A[j][0] 
            #A[i] = [10, 0] -> [num, index], but we just need num to    add          both so we take A[i][0] -> first element is num
            if cur == target:
                # A[i][1] -> gives index of the pair
                # get [smaller, larger] so we use min/max for order of answer
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i+=1
            else:
                j-=1
        return []
