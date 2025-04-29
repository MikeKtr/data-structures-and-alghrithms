
def SCC(Tab):

    n = len(Tab)

    visited = [False for _ in range(n)]
    Time = [0 for _ in range(n)]
    time = 0

    def mini(tab):
        nonlocal visited

        high = 0
        indexHigh = 0
        

        for i in range(n):
            if(visited[i] == False and high < tab[i]):
                high = tab[i]
                indexHigh = i
        return indexHigh

    

    def DFSVisit(Tab,index):
        nonlocal time,visited,Time

        visited[index] = True
        adjacent = Tab[index]
        time += 1



        m = len(adjacent)
        for j in range(m):
            if(visited[adjacent[j]] == False):    
                DFSVisit(Tab,adjacent[j])
        
        Time[index] = time

        time += 1

    for i in range(n):
        if(visited[i] == False):
            DFSVisit(Tab,i)

    def DFSVisit2(tab,index):
        nonlocal visited
        
        adjacent = tab[index]
        visited[index] = True
        m = len(adjacent)
        print(index," ",end="")
        for j in range(m):
            if(visited[adjacent[j]] == False):
                DFSVisit2(tab,adjacent[j])



    reverse = [[] for _ in range(n)]

    for i in range(n):
        for j in Tab[i]:
            reverse[j].append(i)
        
    
     

    visited = [False for _ in range(n)]

    for i in range(n):
        maximum = mini(Time)
        
        DFSVisit2(reverse,maximum)
        print()



graph = [
    [1],          # 0 → 1
    [2],          # 1 → 2
    [0, 3],       # 2 → 0, 3 — (0,1,2) = cykl (SCC 1)

    [4],          # 3 → 4
    [5],          # 4 → 5
    [3, 6],       # 5 → 3 (cykl 3→4→5→3 = SCC 2), oraz 5 → 6

    [7],          # 6 → 7
    [8],          # 7 → 8
    [6],          # 8 → 6 → (6,7,8) = cykl (SCC 3)

    [],           # 9 — samotny, SCC 4
]
SCC(graph)