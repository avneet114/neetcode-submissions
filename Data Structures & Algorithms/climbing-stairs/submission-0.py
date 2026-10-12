"""
Understand: given an integer n representing the number of steps to reach the top of a staircase. 
can climb with either 1 or 2 steps at a time
constraints:
number of steps is between 1 and 45
Match: optimized version of the recursive solution
the key observation is:
- while exploring choices (1 step or 2 step), the same subproblems repeat many times
- for example, the number of ways from step i is always the same whenever we reach i
so instead of recomputing, we store the result the first time we compute it and reuse it later.
this is exactly what top down dynamic programming(memoization) does
Plan:
1. create a cache array cache of size n initiliazed with -1
2. define a recursive function dfs(i):
- if i == n, return 1 (valid array)
- if i > n, return 0 (invalid path)
- if cache[i] != -1, return the cached value
3. otherwise
- compute dfs(i+1) + dfs(i+2)
- store the result in cache[i]
4. return dfs(0) as the final answer
Evaluate: time and space - O(n)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        #create a cache array of size n initialized with -1
        cache = [-1] * n #stores answers that we have already calculated
        #-1 means we haven't calculated this answer yet
        
        def dfs(i): 
            #helper function: return the number of ways to reach the top when currently standing at stair i
            if i >=n: #have we reached or passed the top
                return i == n
            if cache[i] != -1: #check if we already calculated the answer for stair i
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2) # two choices
            return cache[i]
        
        return dfs(0)
