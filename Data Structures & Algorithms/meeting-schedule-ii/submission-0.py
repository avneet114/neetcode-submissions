"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
Understand: given an array of meeting time interval objects consisting of start and end times, find the min number of rooms required to schedule all meetings.
Inputs: list of lists with meeting time intervals
Output: min number of rooms required to schedule all meetings without any conflicts -> max number of overlapping meetings at any given point of time
Constraints: 
0 <= intervals.length <= 100,000
0 <= start < end <= 1,000,000

Edge cases:
- one interval -> return 1
- 0 intervals -> return 0
- overlapping intervals -> different rooms
- end2 = start3 -> consider them non overlapping -> tie with two exact values.

Match: two pointers

we wanna find the min number of rooms required so far that no meetings overlap
instead of tracking whole intervals, we can separate the problem into two simpler timelines:
- one list of all start times
- one list of all end times

if we process these timelines in order:
- whenever a meeting starts before another one ends, we need a new room
- whenever a meeting ends before or at the same time another starts, a room becomes free

by moving two pointers over the sorted start and end times, we can track how many meetings are happening at the same time

the max number of simultaneous meetings at any moment is exactly the number of rooms we need.

Plan:
1. create two arrays:
- start -> all meeting start times, sorted
- end -> all meeting end times, sorted
2. initialize:
- s = 0 -> pointer for start times
- e = 0 -> pointer for end times
count = 0 -> current number of ongoing meetings
res = 0 -> max number of rooms needed
3. while there are still meetings to process (s< number of meetings)
4. if start[s] < end[e]:
- a new meeting starts before the earliest one ends
- increment count (need one more room)
- move s forward
5. else:
- a meeting has ended
- decrement count (a room is freed)
- move e forward
6. update res = max(res,count) after each step
7. return res

Implement:
Review:
Evaluate: 
time - O(n log n)
space - O(n)
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #track count of overlapping times -> return max of this

        #create two arrays
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0,0
        s, e = 0,0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1 
            res = max(res, count)
        return res       
        