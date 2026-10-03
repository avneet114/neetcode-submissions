"""
Understand: Find the kth largest, counting duplicates. For [5,5,4], the 3rd largest is 4.
Match: min-heap to keep track of largest elements seen so far
as min-heap always keeps the smallest element at the top
if we maintain a heap of size k, then
- the heap will always contain the k largest element seen so far
- the root of the heap (the smallest among these k) will be the k-th largest element
plan:
Create an empty min-heap.
Iterate through each number:
Push the number into the min-heap.
If the heap size exceeds k, pop the smallest element.
After processing all numbers, the top of the heap is the k-th largest element.
Return that value.
evaluate:
- time: O(n log k)
- space: O(k)

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num) # add current number to heap

        # If we have more than k numbers, remove the smallest.
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        # We kept the k largest numbers.
        # The smallest of those is the kth largest overall.
        return minHeap[0]

        