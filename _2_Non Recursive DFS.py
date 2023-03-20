def non_recursive_dfs(graph, source):
    if source is None or source not in graph:
        return "Please Enter Valid input"
    path = []
    stack_val = [source]
    while(len(stack_val) != 0):
        s =stack_val.pop()
        if s not in path:
            path.append(s)
        if s not in graph:
            continue
        for neighbor_node in graph[s]:
            stack_val.append(neighbor_node)  
    return " ".join(path)  
graph = {"A":["B","C","D"],  
   "B":["E"],  
   "C":["G","F"],  
   "D":["H"],  
   "E":["I"],  
   "F":["J"],  
   "G":["K"]}  
dfs_element = non_recursive_dfs(graph, "A")  
print(dfs_element)