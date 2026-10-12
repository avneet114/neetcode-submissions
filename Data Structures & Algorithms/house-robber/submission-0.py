"""
Understand: 
Input: an integer array nums where nums[i] represents the amount of money the ith house has
Output: return the max amount of money you can rob without alerting the police
Constraints: can't rob two adjacent houses.
- there's at least one house and max is 100 houses
- the money ith has has can be between 0 or 100
Match: top down dynamic programming problem
at every house, we have two choices:
- skip the current house -> move to the next house (i+1)
- rob the current house -> take its money nums[i] and skip the next house (i+2)

use memoization, each index is solved only once
the goal is to choose the option that gives the max total money

Plan: 
1. create a memo array where memo[i] stores the max money from house i
2. define a recursive function dfs(i):
- if i is out of bounds, return 0
- if memo[i] is already computed, return it
compute:
- skip = dfs(i+1)
- rob = nums[i] + dfs(i+2)
3. store and return max(skip, rob) in memo[i]
4. start recursion from index 0

Implement:
Review:
dry-run
nums = [1,1,3,3]

index each house:
index: 0 1 2 3
money: 1 1 3 3

at first, cache = [-1, -1, -1, -1]
1. we call dfs(0)
- at house 0, we have two choices
skip = dfs(1)
rob = nums[0] + dfs(2)
the code calculates dfs(1) first
2.
dfs(1) -> at house 1
skip = dfs(2)
rob = nums[1] + dfs(3)
again, calculate dfs(2) first

3. dfs(2) at house 2
skip = dfs(3)
rob = nums[2] + dfs[4]

4. calculate dfs(3) at house 3
skip = dfs(4)
rob = nums[3] + dfs(5)
5. calculate dfs(4)
i = 4 is outside the array, so dfs(4) = 0
there skip = 0
now calculate rob option for house 3
rob = nums[3] + dfs(5)
= 3+0
= 3

so cache[3] = max(0, 3)
= 3
return dfs(3) = 3

6. now continue with dfs(2)
skip = dfs(3) = 3
rob = nums[2] + dfs(4)
= 3+0 = 3
therefore
cache[2] = max(3, 3)
= 3
return dfs(2) = 3

current cache = [-1, -1, 3, 3]

7. finish dfs(1)
skip = dfs(2) = 3
rob = nums[1] + dfs(3)
=1+3 = 4
cache[1] = max(3,4)
=4

dfs(1) = 4

current cache = [-1, 4, 3, 4]

8. finish dfs(0)
skip = dfs(1) = 4
rob = nums[0] + dfs(2)
= 1+3 = 4

cache[0] = max(4,4) = 4

return dfs(0) = 4
max amt is 4
Evaluate:
time and space - O(n)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # create a memoization array where cache[i] will store the max amount of money that can be robbed starting from house i
        #-1 means that we haven't computed the answer for house i yet
        cache = [-1] * len(nums) 
        def dfs(i):
            #base case -> if i is past the last house, there is no money left to rob
            if i>=len(nums):
                return 0 # if it goes outta bounds
            #if we alr calculate the answer for house i, return it instead of solving the same subproblem again
            if cache[i] != -1:
                return cache[i] #we haven't computed val so we return that
            #option 1: skip current house and move to next one
            skip = dfs(i+1)
            #option 2: rob current house, take oney, and then skip next one and continue from i+1
            rob = nums[i] + dfs(i+2)
            cache[i] = max(skip, rob) #store max of both in here
            return cache[i]
        #start at house 0, since we can consider every house beginning with the first one
        return dfs(0)

        