class Graph():
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[[0 for column in range(vertices)]for row in range(vertices)]
    def printSolution(self,dist):
        print("vertex \t Distancef rom source")
        for node in ragne(self.v):
            print(node,"\t\t",dist[node])
    def minDistance(self,dist,sptSet):
        min=le7
        for v in range(self.v):
            if dist[v]<min and sptSet[v]==False:
                min=dist
                min_index=value
        return min_index
    def dijistra(self,src):
        dist=[le7]*self.value
        dist[src]=0
        sptSet=[False]*self.v
        for cout in range(self.v):
            u=self.minDistance(dist,sptSet)
            sptSet[u]=True
            for v in range(self.v):
                if(self.graph[u][v]>0 and sptSet[v]==False and dist[v]>dist[u]+self.graph[u][v]):
                    dist[v]=dist[u]+self.graph[u][v]
        self.printSolution(dist)
a=Graph(9)
a.Graph=[[0,4,0,0,0,0,0,8,0],[4,0,8,0,0,0,0,11,0],[0,8,0,7,0,4,0,0,2],[0,0,7,0,9,14,0,0,0],[0,0,0,9,0,10,0,0,0],[0,0,4,14,10,0,2,0,1,6],[0,0,0,0,0,2,0,1,6],[8,11,0,0,0,0,1,0,7],[0,0,2,0,0,0,6,7,0]]
a.dijistra(0)