# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Understand: Given the root of a binary tree, return its values grouped by level, from left to right.
Edge cases:
- Empty tree → []
- One node → [[root.val]]
- A tree with only left or right children → one value per level
Match: BFS with a queue
Plan: 
Create a queue and a result list.
If the root exists, add it to the queue.
While the queue isn’t empty:- Create an empty list for the current level.
- Process exactly the number of nodes currently in the queue.
- Save each node’s value and add its existing children to the queue.
- Add the completed level to the result.
Return the result.
Implement: see below
Review: example on paper
Evaluate:
time: O(N) each node is added to and removed from the queue once.
space: O(n)
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] 
        
        q = deque()
        
        if root:
            q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level)
        return res