# Using a Python dictionary to act as an adjacency list
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = set() # Set to keep track of visited nodes of graph.
#visited=[] to check the order is maintained

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
	visited.add(node)
        #visited.append(node) for adding elements to list
        print("visited:",visited)
        for neighbour in graph[node]:
            print("neighbor:",neighbour)#prints the adjacent nodes
            dfs(visited, graph, neighbour)


print("Following is the Depth-First Search")
dfs(visited, graph, 'A')
 