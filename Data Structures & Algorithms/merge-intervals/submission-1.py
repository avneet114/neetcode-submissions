"""
Understand: We're given intervals, and we need to combine any that overlap. the result should cover the same ranges but none of the returned intervals should overlap.
Input: a list of lists
output: a list of merged intervals such as [[1,6]]

clarifying questions:
- lists
- not sorted
- yes [1,3] and [3,5] should merge
- if input is empty then return []
- negatives are fine, handle duplicates accordingly

Edge cases:
- [] -> []
- [[2,5]] -> [[2,5]]
- touching endpoints merge
- duplicates merge into one -> [1,3]
- not overlap -> return both intervals as is and don't merge them

Match: sorting the intervals by their start times.
Plan:

brute force: first, i could compare every pair of intervals if two overlap, id replace them with one interval using the smaller start and larger end. then id restart checking because the merged interval might overlap another one. id keep doing this untila. complete check finds no overlaps.

time - 0(n^3) in the worst case

Efficient approach using intervals and sorting:
1. sort the intervals by start time
2. create an empty list called merged
3. loop through each interval's start and end. 
4. if merged is empty, we add the interval to it
5. otherwise, compare start with the last merged interval's end
6. if they overlap, we update that end to the larger of the two ends
7. if there's a gap, add a new interval
8. returned merged

Implement: see below
Review:
intervals = [[1,3], [2,6], [8,10], [15,18]]
merged = []
[1,3]
[[1,6], [8,10], [15,18]]

unsorted list and dry run it
[5,7] [1,3] [3,6]
[1,3][3,6][5,7] -> sorted

[1,7]

Evaluate:
time - sorting - O(n log n)
space - O(n)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = []

        for start, end in intervals:
            if not merged:
                merged.append([start, end])
            #if they overlap
            elif start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return merged

        