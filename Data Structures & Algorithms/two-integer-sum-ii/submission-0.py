"""
Using UMPIRE method:
Understand: two sum2
Input: numbers : list[int] -> sorted in ascending order, target int
output: indices of two numbers such that n1+n2=target and index1<index2
constraints:
- index1 and index can't be equal
- can't use same element twice
- space complexity must be O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers)-1

        while numbers[l] + numbers[r] != target:
            current_sum = numbers[l] + numbers[r]
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
        return [l + 1, r+1]

        