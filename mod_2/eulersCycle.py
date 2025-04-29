def eulerCycle(Tab):

    n = len(Tab)

    visitedVertex = [False for _ in range(n)]
    visitedEdges = Tab
    
    currentPath = []

    def DFSVisit(Tab,index):
        
        nonlocal visitedEdges,currentPath

        adjacent = Tab[index]
        m = len(adjacent)

        for j in range(m):
            if(adjacent[j] == 1 and visitedEdges[index][j] == 1):
                visitedEdges[index][j] = 0
                currentPath.append(j)
                DFSVisit(Tab,j)



    
    for i in range(n):
        for k in range(n):
            if(visitedEdges[i][k] == 1):
                currentPath = []
                currentPath.append(i)
                DFSVisit(Tab,i)
                print(currentPath)


graph = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

eulerCycle(graph)