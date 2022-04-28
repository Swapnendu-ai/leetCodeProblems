# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        newGraph = Node(node.val)
        stack = [(neighbor, newGraph) for neighbor in node.neighbors]
        seen = {node.val: newGraph}
        while stack:
            curNode, parent = stack.pop()
            if curNode.val not in seen:
                newNode = Node(curNode.val)
                parent.neighbors.append(newNode)
                stack.extend([(neighbor, newNode)
                             for neighbor in curNode.neighbors])
                seen[curNode.val] = newNode
            else:
                parent.neighbors.append(seen[curNode.val])

        return newGraph
