"""
prefix product = pref[i] = product of all elements to the left of i
suffic product = suff[i] = product of all elements to the right of i

final answer 
result[i] = prefix[i] * suff[i]

plan:
1. let n be the length of the array. create threee arrays of size n
pref for prefix products
suff fro suffic products
res for final result
2. set pref[0] = 1 (nothing to the left of index 0)
suff[n-1] = 1 (nothing to the right of last index)

3. build the prefix product array
for each i from 1 to n-1
pref[i] = nums[i-1] * pref[i-1]

4. build the suffic product array
for each i from n-2 down to 0
suff[i] = nums[i+1] * suff[i+1]

5. build the result 
for each index i, compute:
    res[i] = pref[i] * suff[i]

6. return the result array
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums) # length of array
        res = [0] * n # -> [0, 0 , 0, 0, ... n]
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1 # nothing on left of first elem and rhgt of last elem
        for i in range (1, n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range (n-2, -1, -1):
            suff[i] = nums[i+1] * suff [i+1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

