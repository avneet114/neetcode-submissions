"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
UMPIRE Strategy: 
Understand: We're given meeting intervals in any order, and we return True if the person can attend all of them or false if any meetings overlap.
Input: meeting intervals, each with start and end time
Output: true or false

Clarifying questions:
1. can i sort the input directly? -> yes

Edge cases: 
1. [] -> true cuz no meetings mean no conflicts
2. [[5, 8]] -> true cuz one meeting cannot conflict with another
3. [[0, 8],  [8, 10]] -> true cuz ending exactly when another starts is allowed
4. [[5, 10], [5, 8]] -> false cuz both start at the same time and overlap. 

Match:
sorting problem. 

Plan:
brute force: 
compare every meeting with every other meeting.
two meetings overlap if start1 < end2 and start2 < end1
for each meeting, i check all the meetings after it. that givs usO(n2) time
i only need variables for the two meetings im checking so space is O(1)

we could improve this by sorting first. then we only need to check meetings next to each toher

1. sort the intervals by start time
2. loop from the second meeting to the last
3. get the previous meeting's end time
4. get the current meetings' start time
5. if the current start is less than prvious end, return false
6. otherwise, keep checking the next meeting
7. if we finish without a conflict, return true

Implement: see below
Review: 
1. 
intervals = [[0,30], [5, 10], [15, 20]]
start at [5,10]
prev ends at 30. this starts at 5.
since 5 <30 , they overlap so we return false. 

2. 
intervals  = [[5,8], [9, 15]]
9 > 8 -> true cuz there's no conflict. 

[0, 8] and [8, 10]
8<8 -> false so we return true


Evaluate:
Time complexity: O(n log n)
space complexity: O(n)

"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort meetings
        intervals.sort(key=lambda meeting: meeting.start)

        #start at the second meeting
        for i in range(1, len(intervals)):
            previous_end = intervals[i-1].end
            current_start = intervals[i].start

            #starting before the prev meeting ends mean they overlap
            if current_start < previous_end:
                return False
        
        #no conflicts mean there's no overlap. also handles an empty list
        return True
