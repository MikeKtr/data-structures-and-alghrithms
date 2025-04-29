from collections import deque

def DFS(graf):
    time = 0
    n = len(graf)
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    distance = [-1 for i in range(n)]

    

    def DFSvisit(graf,i):
        nonlocal time
        visited[i] = True
        # print(graf[i])
        m = len(graf[i])
        time += 1
        for j in range(m):
            if(visited[j] == False):
                visited[j] = True
                parent[j] = i
            
                DFSvisit(graf,j)
        time+=1
    for i in range(n):
        if(visited[i] == False):
            DFSvisit(graf,i)


    
