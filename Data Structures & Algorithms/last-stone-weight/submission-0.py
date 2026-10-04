"""
Understand: 
Input: an array of integers stones where stones[i] are the weights of the ith stone
Simulation:
1. choose two heaviest stones with weight x and y and smash them together
2. if x == y -> destroy both
3. if x<y, the stone of weight x is destroyed while stone of weight y has new weight = y-x
5. continue the simulation until there's just one stone remaining
6. return the weight of the last stone or return 0 if none remain
edge cases:
- there's just one stone -> return the weight of that stone
- no stone remains if the last stones were equal to each other- return 0
intuition
- most languages provude min-heaps so a common trick is to store negative values. this makes the smallest (most negative) value represent the largest stone 
Match: max-heap
Plan:
onvert every stone weight x into -x and build a min-heap.
While the heap contains more than one stone:
Pop two values a and b (these represent the two heaviest stones).
If a != b, compute the remaining stone weight:
diff = a - b (still negative)
Push diff back into the heap.
After the loop:
If the heap is empty, return 0.
Otherwise return the absolute value of the remaining stone.
evaluate:
- time: O(n log n)
- space: O(n)
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python's heapq is a min-heap, so negate every weight.
        # The largest original stone becomes the smallest negative value.
        # Example: [2, 6, 4] -> [-2, -6, -4]
        stones = [-s for s in stones] 
        heapq.heapify(stones) #rearrange the list into a valid min-heap. the smallest value (heaviest stone will be at index 0)

        #continue while at least two stones remain:
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first-second)
        stones.append(0) #add 0 so heap is never emoty. if no stones remain, stones[0] becomes o
        return abs(stones[0]) #convert the remaining negative weight back to positive
 
        
        