"""
Understand: container with most water - use two bars to form a container
Input: heights : list[int] where heights[i] represents height of the ith bar
Output: max amount of water a container can store.
area = width * height
width = right_index - left_index  (horizontal distance b/w two bars)
7-1 = 6 or 5-1 = 4? 
height = 7 or 6
6*6 = 36 > 4*7 = 28
height = min(heights[left], heights[right])
water sits between two walls. No matter how tall one wall is, water will spill over the top of the shorter wall 
so the water level (and thus the container's usable height) is always capped by whichever of the two chosen bars is shorter. The taller one contributes nothing beyond that cap.
Match: two pointers
Plan:
- initialize two points l=0, r = len(heights)-1
set res=0 to store max area
while l<r
- compute the current area
area = min(heights[l], heights[r] * (r-l)) 
- update res with max area so far
move the pointer at shorter height
- if heights[l] <= heights[r], move l right
- otherwise move r left
return res after pointers meet

"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l<r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l+= 1
            else:
                r-=1
        return res
        