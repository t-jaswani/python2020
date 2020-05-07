graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}
visited = [A,B,S,C] # where the visited nodes are going to be stored
def dfs(graph, node, visited):
    print("The value of the node is: ", node)
    if node not in visited: # checks if node being visited is in the visited list
        #print("The new node is:",node)
        visited.append(node) # Adds to the visited node
        for n in graph[node]:
            #print("The value of n is:", n)
            dfs(graph,n, visited)
    return visited
visited = dfs(graph1,'A', visited)
print(visited)
A{B{A},S{A,C,G}}

#A{B{A},S{A,C{D{C},E{C,H},F,},G}}



#A{B{A}, S{A,C{D{C},E{C,H{E{C,H},G{F{C,G},S}}},F,S},G} }


