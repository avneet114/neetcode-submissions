"""
time - O(n log n)
space - O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # create a hashmap to store the frequency of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num]) # build a list of [freq, num] pairs from the map
        arr.sort() # sort the list in ascending order based on frequency

        res = [] # create an empty results list
        while len(res) < k: #stop when result contains k elements
            res.append(arr.pop()[1]) # repeatedly pop from the end of sorted list and append the number to the result
        return res # return the result list
        