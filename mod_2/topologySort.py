def topologySort(Tab,max):

    n = len(Tab)

    visited = [False for _ in range(n)]


    def DFSVisit(Tab,index):
        nonlocal visited
        
        visited[index] = True

        adjacent = Tab[index]

        m = len(adjacent)

        for j in range(m):
            if(visited[adjacent[j]] == False):
                DFSVisit(Tab,adjacent[j])
    
        print(index , end =" <- ")

    for i in range(n):
        if(visited[i] == False):
            DFSVisit(Tab,i)
graph = [
    [1, 2], # 0 -> 1, 2
    [3, 4], # 1 -> 3, 4
    [5],    # 2 -> 5
    [6],    # 3 -> 6
    [6],    # 4 -> 6
    [7],    # 5 -> 7
    [7],    # 6 -> 7
    []      # 7 -> (brak wyjść)
]

topologySort(graph,5)
print("None")