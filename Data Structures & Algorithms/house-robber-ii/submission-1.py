#difference is first and last elements are adjacent to each other. houses are in a circle
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = [[-1] * 2 for _ in range(len(nums))]
        #creates a 2D list with len(nums) rows - one for each house index i and 2 columns - onefor each possible flag value
        #memo[i][flag] stores best amount obtainable starting at house i
        # two possible values are flag
        # 0/false or 1/true -> -1 means the state hasn't been calculated yet

        #flag records whether the first house was robbed
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) -1):
                #we passed the final house or flag is true and i the last house so last house is forbidden
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            
            skip = dfs(i+1, flag)
            rob = nums[i]+dfs(i+2, flag or (i==0)) #sets flag to true if house 0 is robbed. that means last house must be avoided
            memo[i][flag] = max(skip, rob)
            return memo[i][flag]
        return max(dfs(0, True), dfs(1, False))
        #last house is treated unavailable -. dfs(0, True) -> 0 through n-2
        # dfs(1, False) -> 1 through n-1

        