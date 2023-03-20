<<<<<<< HEAD
def dfs_recursive(graph, source,path = []):  
  
       if source not in path:  
           path.append(source)  
  
           if source not in graph:  
               # leaf node, backtrack  
               return path  
  
           for neighbour in graph[source]:  
  
               path = dfs_recursive(graph, neighbour, path)  
        return path  
      
graph = {"A":["B","C","D"],  
   "B":["E"],  
   "C":["G","F"],  
   "D":["H"],  
   "E":["I"],  
   "F":["J"],  
   "G":["K"]}  
dfs_element = dfs_recursive(graph, "A")  
=======
def dfs_recursive(graph, source,path = []):  
  
       if source not in path:  
           path.append(source)  
  
           if source not in graph:  
               # leaf node, backtrack  
               return path  
  
           for neighbour in graph[source]:  
  
               path = dfs_recursive(graph, neighbour, path)  
        return path  
      
graph = {"A":["B","C","D"],  
   "B":["E"],  
   "C":["G","F"],  
   "D":["H"],  
   "E":["I"],  
   "F":["J"],  
   "G":["K"]}  
dfs_element = dfs_recursive(graph, "A")  
>>>>>>> 6d4c0bdaf237af1555cf484289d2fa8b6668d854
print(dfs_element)