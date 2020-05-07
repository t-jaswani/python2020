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

def dfs(graph,node):
    print("the starting node is:", node)
    visited = [node] # keeps track of the visited 
    stack = [node] # helps in keeping track of the nodes to be visited next 
   
# big O notation = O(n**2)

    while stack: #!= null
        node = stack[-1] # what does this do? assign the last element to 
        print("the value of node in the loop is: ", node)
        if node not in visited:
            print("Node that is been visited for the first time is: ", node)
            visited.extend(node) # what does the extend  keyword do? joins two lists together. add node list to visited list. 
        remove_from_stack = True
        for next in graph[node]: #a,c,g

            if next not in visited:
                stack.extend(next)
                print("contents inside stack are: ", stack)
                print("Contents inside visited are: ", visited)
                remove_from_stack = False #what does this do?
                break #what does the break keyword do? if it get stuck in infinte loop it will break the loop
        if remove_from_stack: # ==True
            
            stack.pop() # what does pop do? remove from end of the list
            print("Final value in stack is:", stack)
            print("Final value in visited is: ", visited)
    return visited

print (dfs(graph1, 'A'))
"""
Visted = [a,b,s,c]
Stack = (a,c)
node = c 
"""
