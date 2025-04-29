


def findBridges(G):

    n = len(G)

    visited = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    low = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    wyniki = []
    time = 0



    def DFSvisit(G,index):
        nonlocal time,wyniki
    


        adjacent = G[index]
        m = len(adjacent)

        time += 1

        distance[index] = time
        low[index] = time
        visited[index] = True
        


        lowestLow = float('inf')
        lowestReverse = float('inf')

        for j in range(m):
            if(visited[adjacent[j]] == False):
                parent[adjacent[j]] = index
                DFSvisit(G,adjacent[j])
                lowestLow = min(lowestLow,low[adjacent[j]])
            elif(adjacent[j] != parent[index]):
                lowestReverse = min(distance[adjacent[j]],lowestReverse)

            
        
        low[index] = min(lowestLow,lowestReverse,distance[index])

        

    for i in range(n):
        if(visited[i] == False):
            DFSvisit(G,i)

    for i in range(n):
        if(parent[i] != None and distance[i] == low[i]):
            wyniki.append((i,parent[i]))
    print(wyniki)

graph5 = [
    [1, 2],          # 0
    [0, 2, 3],       # 1
    [0, 1],          # 2
    [1, 4, 5],       # 3
    [3],             # 4
    [3, 6, 7],       # 5
    [5, 7],          # 6
    [5, 6, 8],       # 7
    [7, 9],          # 8
    [8]              # 9
]
findBridges(graph5)