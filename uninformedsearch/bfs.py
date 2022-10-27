graph = {
  'P' : ['Q','R','S'],
  'Q' : ['P', 'R'],
  'R' : ['P','Q','T'],
  'S' : ['P'],
  'T' : ['R'],
  
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      print("\nneighbor:",neighbour)
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        print("queue:",queue)


print("Following is the Breadth-First Search")
bfs(visited, graph, 'P')    # function calling