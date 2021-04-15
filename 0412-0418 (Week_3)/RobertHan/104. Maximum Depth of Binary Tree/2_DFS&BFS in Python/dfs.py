# DFS(Depth-First Search)
""" 
- Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

- DFS is initialized by a Stack(or recursive function)
Depends on policy(which is differ from questions, how to access near node)
1. Add first Node in the stack, and mark as 'visited(or discorvered)'
2. If there is connected Node which is not saveed in Stack, put it in the Stack and mark it as 'visited'
3. Iterate 2 till there is no node.
"""

def dfs(graph, v, visited):
    
    visited[v] = True
    print(v, end=' ')
    # Visit connect node
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# Graph
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

# Call the function 
dfs(graph, 1, visited)