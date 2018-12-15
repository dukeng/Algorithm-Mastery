


## How to check if an undirected graph contain cycle? 
http://www.techiedelight.com/check-undirected-graph-contains-cycle-not/
Answer: Do a BFS or DFS from any node and keep track of back-edge.

## Topological Sort for DAG using DFS and Kahn's Topological sort
### Think about partial order
Implemented in technics


## Transitive Closure of a Graph
http://www.techiedelight.com/transitive-closure-graph/

## Graph Bipartite
http://www.techiedelight.com/bipartite-graph/

A Bipartite graph is a graph such that vertices can be divivded into 2 separated sets and every vertex connects two vertices in different sets

How to check if a graph is bipartite?
Do graph coloring. Do a bfs from any node, start with marking that node as red. Repeatedly flip the color for the neighbors. When encountering a neighbor with the same color as the current node, then it's not a bipartite graph.

## Back edge, forward edge, cross edge definition
http://www.techiedelight.com/types-edges-involved-dfs-relation/


## Ways to solve:
### Find if Undirected graph with cycle?
Run BFS from any node to see if there is anything repeated in visited()
### Directed graph with/without cycle?
??? 
### Directed Acylic graph.
???