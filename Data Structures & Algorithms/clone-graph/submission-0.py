"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
UMPIRE Strategy:
Understand: 
Input: a node in a connected undirected graph containing an integer val and list of its neighbors
Output: a deep copy of the graph
An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.
The graph may contain cycles, so we cannot simply copy nodes recursively without remembering what we've already copied.
To handle this, we use a map (old → new):

When we first see a node, we create its copy.
If we see the same node again, we reuse the already-created copy.
This avoids infinite loops and ensures each node is cloned exactly once.
Depth First Search (DFS) helps us explore and clone all connected nodes.
Match: BFS Adjacency list
Plan:
1. If the input node is null, return null.
2. Create a map to store original nodes -> cloned nodes.
3. Start DFS from the given node:
- If the node is already in the map, return its clone.
- Create a new node with the same value.
- Store it in the map.
- Recursively clone all neighbors and add them to the clone’s neighbor list.
4. Return the cloned node corresponding to the starting node.

Implement:
Review:
Time - O(v+e), where v = number of vertices and e = number of edges
space - O(v)
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: #value can be a node or none
        oldToNew = {} #create a dict that maps each og node to its cloned node -> this prevents cloning the same node more than once and prevents infinite recursion when graph contains cycles

        def dfs(node): #nested recursive dfs function
            if node in oldToNew: #check if the og node has alr been cloned.
                return oldToNew[node] #if it has, return the exisiting clone instead of creating a new one
            
            copy = Node(node.val) #creates a new copy with same value as original node
            oldToNew[node] = copy #stores the relationship between og node and its clone
            for nei in node.neighbors: #loop thru every neighbor of the current og node
                copy.neighbors.append(dfs(nei)) 
                #call dfs(nei) to clone the neighbor
                #receives the neighbor's clone
                #adds that to the current copied node's neighbor list
            return copy
        return dfs(node) if node else None #handles the empty graph case
        
        