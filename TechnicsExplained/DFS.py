import sys

# Node object
class Node():
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        self.edges = dict() # map neighbors -> distances

    def add_neighbors(self, listVal):
        for val in listVal:
            self.neighbors.append(val)

def DFS(hm):
    visited = set()
    def recur_DFS(node):
        print(node.val)
        visited.add(node.val)
        for neighbor in node.neighbors:
            if neighbor.val not in visited:
                recur_DFS(neighbor)
    for node in list(hm.values()):
        if node.val not in visited:
            recur_DFS(node)

def test_dfs():
    hm = dict()
    hm[0] = Node(0)
    hm[1] = Node(1)
    hm[2] = Node(2)
    hm[3] = Node(3)
    hm[4] = Node(4)
    hm[5] = Node(5)
    hm[6] = Node(6)

    hm[0].neighbors = [hm[1],hm[3]]
    hm[1].neighbors = [hm[2],hm[3]]
    hm[3].neighbors = [hm[0],hm[2],hm[4]]
    hm[5].neighbors = [hm[6]]
    hm[6].neighbors = [hm[3]]
    DFS(hm)
# test_dfs()

def DFS_test_edges(hm, root):
    start = dict()
    end = dict()
    back_edge = []
    cross_edge = []
    forward_edge = []
    tree_edge = []
    time = 1
    def recur_DFS(node, time):
        start[node.val] = time
        for neighbor in node.neighbors:
            print(neighbor.val, start, end)
            if neighbor.val in start and neighbor.val not in end:
                back_edge.append([node.val, neighbor.val])
            elif neighbor.val in end:
                if start[neighbor.val] > start[node.val]: # neighbor started after the node, which implies forward
                    forward_edge.append([node.val, neighbor.val])
                else:
                    cross_edge.append([node.val, neighbor.val])
            else:
                tree_edge.append([node.val, neighbor.val])
                time = recur_DFS(neighbor, time + 1)
        
        end[node.val] = time
        return time + 1
    recur_DFS(root, time)
    print(start, end)
    print("back", back_edge)
    print("forward",forward_edge)
    print("cross",cross_edge)
    print("tree",tree_edge)

def testDFSTestEdge():
    # image: https://cs.stackexchange.com/questions/11116/difference-between-cross-edges-and-forward-edges-in-a-dft
    hm = dict()
    hm[1] = Node(1)
    hm[2] = Node(2)
    hm[3] = Node(3)
    hm[4] = Node(4)
    hm[5] = Node(5)
    hm[6] = Node(6)
    hm[7] = Node(7)
    hm[8] = Node(8)

    hm[1].neighbors = [hm[2],hm[5],hm[8]]
    hm[2].neighbors = [hm[3]]
    hm[3].neighbors = [hm[4]]
    hm[4].neighbors = [hm[2]]
    hm[5].neighbors = [hm[6]]
    hm[6].neighbors = [hm[3], hm[7], hm[8]]
    DFS_test_edges(hm, hm[1])

testDFSTestEdge()