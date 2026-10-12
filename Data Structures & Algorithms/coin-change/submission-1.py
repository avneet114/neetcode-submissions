"""
Understand: Coin Change
Input: integer array of coins that represents coins of different denominations (1 dollar,5 dollars, etc) and an inetger amount representing target amt of money
Output - fewest number of coins that we need to makeup the exact target amount. if impossible, return -1
assume: we have unlimited number of each coin so we can use a coin ore than once
- we don't have to use EVERY kind coin available
- if amount is 0 then amt of coins needed = 0
Match: DP (top-down)
Plan:
Use a hashmap memo to store results for already computed amounts
Define dfs(amount):
If amount == 0, return 0
If amount exists in memo, return it
Try every coin:
If amount - coin >= 0
Compute 1 + dfs(amount - coin)
Track the minimum
Store the result in memo[amount]
Return the stored value
If the final answer is still very large, return -1

Implement: See below
Review:
coins = [1,5,10]
amount = [12]

1. I will define dfs(amount) to return the minimum number of coins needed to make this amount. and if an amount if impossible, we return -1
2. if the remaining amount if 0, i need zero more coins so i return 0
3. for recursive choices:
- for each coin that does not exceed the current amount, i use that coin and recursively solve the remaining amount

for amount 12:
    use 1 -> solve 11
    use 5 -> solve 7
    use 1o -> solve 2

3. after solvign each position, I add 1 for the coin i just used and take the minimun
4. For the 10 coin, the remaining amount is 2. The best way to make 2 is two 1 coins, so that choice uses 1 + 2 = 3 coins total. Other choices are evaluated as well, and the minimum is 3
5. explain memoization: Different recursive paths can ask for the same remaining amount. Once I compute an amount, I store its result in memo, so future calls return it immediately

6. for example: 
if memo[amount] != -1:
    return memo[amount]
This prevents recomputing the same subproblem

7. Internally, I use infinity to indicate that an amount is impossible. After solving the original amount, if the result is still infinity, I return -1; otherwise I return the minimum coin count.


Evaluate:
time - O(n * t) -> where n is the length of array coins and t is the given amount
space - O(t)
There are amount + 1 possible states, and for each state I try every coin. Therefore the time complexity is O(amount * len(coins)), and the memoization plus recursion stack uses O(amount) space
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #memo is storing an answer for each possible remaining amount
        memo = [-1] * (amount + 1)
        
        def dfs(amount):
            if amount == 0:
                return 0
            if memo[amount] != -1:
                return memo[amount]
            res = 1e9 #one billion or infinity -> impossible to make this remaining amount
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount-c))
                
            
            memo[amount] = res
            return res
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
