n=4
def printsolution(sol):
    for i in sol:
        for j in i:
            print(str(j)+' ',end='')
        print()
def issafe(maze,x,y):
    if x>=0 and x<n and y>=0 and y<n and maze[x][y]==1:
        return True
    return False
def solvemaze(maze):
    sol = [ [ 0 for j in range(4)] for i in range(4)]
    if solvemazeutil(maze,0,0,sol)==False:
        print('solution does not exist')
        return False
    printsolution(sol)
    return True
def solvemazeutil(maze,x,y,sol):
    if x==n-1 and y==n-1:
        sol[x][y]=1
        return True
    if issafe(maze,x,y)==True:
        sol[x][y]=1
        if solvemazeutil(maze,x+1,y,sol) == True:
            return True
        if solvemazeutil(maze,x,y+1,sol) == True:
            return True
        sol[x][y]=0
        return False
if __name__ == "__main__":
    maze=[ [1,0,0,0], 
        [1,1,0,1], 
            [0,1,0,0], 
            [1,1,1,1] ]
    solvemaze(maze)