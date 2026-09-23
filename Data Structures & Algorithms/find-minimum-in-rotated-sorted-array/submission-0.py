"""
Understand:
Input: array nums of length n that's been rotated 1to n times after being sorted
Output: the min element in the array
Match: binary search
Plan: brute force 
return min(nums) -> it's not efficient. O(n) we need to find O(log n)

Intuition: 
a rotated sorted array has one special property: one part is always sorted, and the other part contains the rotation (and the minimum element)
nums[mid] >= nums[left] -> search right
else search left
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r-l) // 2
            if nums[m]  < nums[r]: #compare middle value with rightmost val -> then min lies in the left half
                r = m
            else: #otherwise the min lies in the right half excluding mid
                l = m+1
        return nums[l]

        