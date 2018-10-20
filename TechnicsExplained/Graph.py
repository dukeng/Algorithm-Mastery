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

# BFS on a directed graph
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

############# Dijkstra ###############
# Dijkstra on a directed graph. Dijkstra have to run throughoutly. Can't tell if the distance is minimum if not run throughoutly
# Does not work on negative weights. Use a greedy approach
# I use a priority queue on edge while Wikipedia uses a pq on node
def Dijkstra(hm_vertices, start):
    import heapq
    heap = []
    # init distances from start to every other vertices
    distances = dict()
    for nodeName, node in hm_vertices.items():
        distances[nodeName] = sys.maxsize
    distances[start] = 0
    for to, value in hm_vertices[start].edges.items():
        heapq.heappush(heap,(value, start, to))
    parent = dict() # map node to the previous node
    result = []
    while heap:
        value, from_, to_ = heapq.heappop(heap)
        if  value >= distances[to_]:
            continue
        distances[to_] = value 
        parent[to_] = from_
        for toNode, edge_distance in hm_vertices[to_].edges.items():
            heapq.heappush(heap, (edge_distance + distances[to_], to_, toNode)) # maybe optimize this
    return distances, parent


def Dijkstra_test():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")

    A.add_neighbors(['B','C'])
    B.add_neighbors(['E','C'])
    C.add_neighbors(['D'])
    D.add_neighbors(['C'])
    E.add_neighbors(['B','C', 'D'])

    A.edges['B'] = 10
    A.edges['E'] = 3
    B.edges['E'] = 4
    B.edges['C'] = 2
    C.edges['D'] = 9
    D.edges['C'] = 7
    E.edges['B'] = 1
    E.edges['C'] = 8
    E.edges['D'] = 2

    hm_vertices = dict()
    hm_vertices["A"] = A
    hm_vertices["B"] = B
    hm_vertices["C"] = C
    hm_vertices["D"] = D
    hm_vertices["E"] = E
    order = Dijkstra(hm_vertices, 'A')
    print(order)
Dijkstra_test()

############# Topological Sort #############

def TopologicalSort(hm_vertices):

    def find_no_incoming_edge(temp_hm_vertices):
        pointed_to = set()
        not_pointed_to = []
        for name, vertice in temp_hm_vertices.items():
            for neighbor in vertice.neighbors: 
                pointed_to.add(neighbor)
        for name, vertice in temp_hm_vertices.items():
            if name not in pointed_to:
                not_pointed_to.append(name)
        return not_pointed_to

    sorted_list = []
    visited = set()
    no_incoming_edge = []      

    no_incoming_edge += find_no_incoming_edge(hm_vertices)

    while no_incoming_edge:
        node = no_incoming_edge.pop()
        if node not in visited:
            visited.add(node)
            sorted_list.append(node)
            del hm_vertices[node]
        no_incoming_edge += find_no_incoming_edge(hm_vertices)
    
    if hm_vertices:
        return []
    else:
        return sorted_list
            
def Topological_sort_test():
    # Visualization: http://www.techiedelight.com/kahn-topological-sort-algorithm/
    zero = Node("0")
    one = Node("1")
    two = Node("2")
    three = Node("3")
    four = Node("4")
    five = Node("5")
    six = Node("6")
    seven = Node("7")

    zero.add_neighbors(["6"])
    one.add_neighbors(['2','4','6'])
    three.add_neighbors(['0','4'])
    seven.add_neighbors(['0','1'])
    five.add_neighbors(['1'])

    hm_vertices = dict()
    hm_vertices["0"] = zero
    hm_vertices["1"] = one
    hm_vertices["2"] = two
    hm_vertices["3"] = three
    hm_vertices["4"] = four
    hm_vertices["5"] = five
    hm_vertices["6"] = six
    hm_vertices["7"] = seven
    order = TopologicalSort(hm_vertices)
    print(order)
# Topological_sort_test()


############# Union Find #############

class UnionFind(): # Kruskal below depends on this 
    def __init__(self, numbers):
        self.parent = dict()
        self.rank = dict()
        for num in numbers:
            self.parent[num] = num
            self.rank[num] = 0
    
    def Find(self,a):
        if self.parent[a] != a:
            self.parent[a] = self.Find(self.parent[a])
        return self.parent[a]

    def Union(self, a, b):
        x = self.Find(a)
        y = self.Find(b)
        if (x == y):
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] += 1
         

def UnionFindTest():
    union_find = UnionFind([i for i in range(5)])
    union_find.Union(0,1)
    union_find.Union(1,2)
    print(union_find.parent)
    union_find.Union(2,4)
    print(union_find.parent)
# UnionFindTest()

############# Minimum Spanning Tree #############

def Kruskal(hm_vertices, vertices):
    nodeNames = []
    for nodeName in hm_vertices:
        nodeNames.append(nodeName)
    uf = UnionFind(nodeNames)
    chosen_edges = []
    vertices = sorted(vertices, key= lambda x : x[0])
    while len(chosen_edges) < len(nodeNames) - 1:
        vertex = vertices.pop(0)
        if uf.Find(vertex[1]) == uf.Find(vertex[2]):
            continue
        uf.Union(vertex[1], vertex[2])
        chosen_edges.append(vertex)
    return chosen_edges

def KruskalTest():
    hm_vertices = [i for i in range(7)]

    vertices = []
    vertices.append([7,0,1])
    vertices.append([5,0,3])
    vertices.append([8,2,1])
    vertices.append([5,2,4])
    vertices.append([9,1,3])
    vertices.append([7,4,1])
    vertices.append([15,4,3])
    vertices.append([6,3,5])
    vertices.append([8,5,4])
    vertices.append([9,6,4])
    vertices.append([11,5,6])

    order = Kruskal(hm_vertices, vertices)
    print(order)

KruskalTest()