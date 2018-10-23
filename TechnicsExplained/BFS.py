import sys

# Node object
class Node():
    def __init__(self, val):
        self.node = val
        self.neighbors = []
        self.edges = dict() # map neighbors -> distances

    def add_neighbors(self, listVal):
        for val in listVal:
            self.neighbors.append(val)

# Basic BFS on a directed graph
def BFS(root):
    if not root:
        return []
    queue = [root]
    visited = set()
    result = []
    while queue:
        node = queue.pop(0)
        visited.add(node.val)
        result.append(node.val)
        for neighbor in node.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)
    return result


# BFS Check if graph contain cycle(both directed and undirected)
# Assume pass in a root which has no parent
# Some problem has to find the root
def BFS_cycle(root):
    queue = [root]
    visited = set()
    result = []
    parent = dict()
    def find_cycle():

    while queue:
        node = queue.pop(0)
        visited.add(node.val)
        result.append(node.val)
        for neighbor in node.neighbors:
            if neighbor.val not in visited:
                parent[neighbor.val] = node.val
                queue.append(neighbor)
            else: # back edge, neighbor.val visited
                find_cycle(node,neighbor.val)
                
    return result    
