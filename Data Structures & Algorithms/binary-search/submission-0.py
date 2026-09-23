"""
Understand: binary search
input: an array of distinct integers "nums", sorted in ascending order, and an integer "target"
Output: return index of the target within nums if it exists, otherwise return -1
Constraints:
Time complexity has to be O(log n) time
edge cases:
array is empty -> return -1
Match: binary search
Plan:

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = l+((r-l) // 2)
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        return -1  