"""
Understand:
Match - queue + maxHeap
Intuition
We always want to run the task that still has the most remaining occurrences, because those are the hardest to fit into the schedule (they need more slots with cooldown gaps).

So we:

Keep a max-heap of tasks by their remaining count (most frequent on top).
At each time unit, we take the most frequent available task and run it.
After running a task, it goes into a cooldown queue with the time when it will be available again (current time + n).
When a task’s cooldown finishes, we push it back into the heap so it can be scheduled again.
If the heap is empty but some tasks are still in cooldown, we can jump the current time forward to the next time when a task becomes available.
This way we always use the CPU as efficiently as possible while respecting the cooldown.

Algorithm
Count how many times each task appears.
Build a max-heap where each entry is "remaining count" of a task (the higher the count, the higher its priority).
Create an empty queue (FIFO) to store pairs: (remaining_count_after_running, next_available_time).
Set time = 0.
While the heap is not empty or the cooldown queue is not empty:
Increment time by 1.
If the heap is not empty:
Pop the task with the largest remaining count.
"Run" it once: remaining_count -= 1.
If remaining_count > 0, push (remaining_count, time + n) into the cooldown queue (it can be used again after n units).
Check the front of the cooldown queue:
While the task at the front has next_available_time == time,
remove it from the queue and push its remaining_count back into the max-heap.
(Optional optimization)
If the heap is empty and the cooldown queue is not empty:
Let next_time be the next_available_time of the front element in the cooldown queue.
Set time = next_time (fast-forward), then process step 3 again for that time.
When both the heap and cooldown queue are empty, return time as the minimum time required to finish all tasks.
Time: O(T*n)
sPACE: O(t) where t is the time to process given tasks an n is the cooldown time
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #each task 1 unit time
        #minimize idle time

        count = Counter(tasks) #hashmap provided by python
        maxHeap = [-cnt for cnt in count.values()]

        #turn array into heap
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # we have -ve values
                if cnt: #is non zero
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time