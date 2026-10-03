# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understand - given the root of a bst and an integer k, return the kth smallest value (1-indexed) in the tree
edge cases:
- tree's empty -> can't find the smallest value -> return -1
- kth value isn't in tree -> return false
inorder travel (left-node-right)
Match: inorder traversal dfs, arrays
Plan:
- do an inorder traversal
- this automatically produces values in ascending order
- the k-th element in this inorder list is the answer
1. create an empty list[]
2. perform inorder dfs:
- visit the left subtree
- add the current node's value to the list
- visit the right subtree
3. after traversal, list will be sorted
4. return list[k-1]
Implement:
Review:
Evaluate: 
- time - O(n)
- space - O(n)
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list = []

        def inorder(root):
            if not root: # root's empty
                return -1 
            
            inorder(root.left)
            list.append(root.val)
            inorder(root.right)

        inorder(root)
        return list[k-1] #cuz it's 1 indexed but k is 0 indexed

        