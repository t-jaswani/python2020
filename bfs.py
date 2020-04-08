graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}


visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  print("Visited -------------->", visited)
  queue.append(node)
  print("Queue------------------>",queue)

  while queue:
    s = queue.pop(0) 
    print("The value of s is....",s)
    print (s, end = " \n") 
    #print("current in queue---------------->", queue)

    for neighbour in graph[s]:
      if neighbour not in visited:
        print("current in queue before---------------->", queue)
        visited.append(neighbour)
        queue.append(neighbour)

        
        print("Values that have been visited--->", visited)

bfs(visited, graph, "A")