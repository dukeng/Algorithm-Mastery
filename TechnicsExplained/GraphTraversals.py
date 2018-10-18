

# Node object
class Node():
    def __init__(self, val):
        self.node = val
        self.neighbors = []

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



############# Topological Sort ###############


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

Topological_sort_test()
