
def SCC(tab):
    time = 0
    n = len(tab)
    visited = [False for _ in range(n)]
    distance = [None for _ in range(n)]
    time = 0
    def max_index(tab):
        maxi = 0
        maxv = 0
        for i in range(len(tab)):
            if(maxv < tab[i]):
                maxi = i
                maxv = tab[i]

        return maxv,maxi

    def DFSvisit(tab,i):
        print("wchodze do dfs: " , i)
        nonlocal time,visited,distance
        visited[i] = True
        m = len(tab[i])
        for j in range(m):
            if(visited[tab[i][j]] == False):
                
                DFSvisit(tab,tab[i][j])
        # print(i)
        distance[i] = time
        time +=1
        print("wychodze z dfs: " , i)

    for i in range(n):
        if(visited[i] == False):
            DFSvisit(tab,i)
    print(distance)

    tab2 = [[] for _ in range(n)]
    for i in range(n):
        m = len(tab[i])
        for j in range(m):
            tab2[tab[i][j]].append(i)

    print(tab2)
    print(visited)
    
    def DFSvisit2(tab2,i):
        nonlocal visited,distance
        visited[i] = False
        distance[i] = 0
        print(i,end=":")

        m = len(tab2[i])
        for j in range(m):
            # print(tab2[i][j])
            if(visited[tab2[i][j]] == True):
                # print(tab2[i][j])
                DFSvisit2(tab2,tab2[i][j])


    maxv,maxi = max_index(distance)
    while(maxv != 0):
        # distance[maxi] = 0
        DFSvisit2(tab2,maxi)

        

        
        maxv,maxi = max_index(distance)



graph = [
    [1],        # 0 → 1
    [2],        # 1 → 2
    [3],        # 2 → 3
    [0,6,1],     # 3 → 0, 1,6 (SCC1: cykl 0→1→2→3→0 + wewnętrzne krawędzie)

    [5],        # 4 → 5
    [4,7, 6,0],     # 5 → 4,7,0(cykl w SCC2 + wyjście do SCC3)

    [7, 8],     # 6 → 7, 8
    [6, 8],     # 7 → 6, 8
    [6]         # 8 → 6 (SCC3: 6 ↔ 7 ↔ 8 ↔ 6, pełne sprzężenie)
]

SCC(graph)