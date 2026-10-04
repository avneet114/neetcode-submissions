"""
Using UMPIRE strategy:
Understand: 
Input: 2-d array of points where points[i] = [xi, yi] are coordinates of a point on X-Y axis plane. we're also given an integer k
Output - return the k closest points to the origin (0,0)
distance = (sqrt((x1c- x2)^2 + (y1 - y2)^2))
Match - minHeap -> gives us the smallest element first
If we insert every point into a min-heap, using its squared distance from the origin as the priority, then:

The closest point will be at the top.
The next closest will be removed next, and so on.
So if we remove from the heap k times, we get exactly the k closest points.

This works because the heap always keeps the smallest distances at the front.
Plan:
For each point (x, y):
Compute squared distance x^2 + y^2.
Store (distance, x, y) as a heap entry.
Build a min-heap from all entries.
This can be done with one heapify operation, or by pushing entries one at a time.
Repeat k times:
Remove the smallest element from the heap.
Add its (x, y) coordinates to the result.
Return the result list of k closest points.
Implement: see below
Review:
Evaluate: 
Time - O(n + k*log n) when building the heap with heapify
Space: O(n)
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # just a list for now

        for x, y in points: #go thru every point
            dist = (x ** 2) + (y ** 2) #(x^2 + y^2 in python)
            minHeap.append([dist, x, y]) #key value for minHeap is dist so we sort by dist. smallest goes first
        
        heapq.heapify(minHeap) #turn list to heap so it reorder it so it's i structure of list
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap) #get three values we pop
            res.append([x, y]) #just add coordinates
            k -=1 # we do it k times so remember to decrement
        return res        