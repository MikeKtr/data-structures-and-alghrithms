from zad3testy import runtests
from collections import deque


def BFS(graf,i,end):
    n = len(graf)
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    result = []
    q = deque()

    q.append(i)
    visited[i] = True
    ile = 0
    while q:
        index = q.popleft()

        i = graf[index]

        for j in range(len(i)):

            if visited[i[j]] == False:
                visited[i[j]] = True
                parent[i[j]] = index
                 
                if(i[j] == end):
                    
                    k = parent[i[j]]
                    result.append(i[j])
                    while(k != None):
                        result.append(k)
                        k = parent[k]
                    return result
                q.append(i[j])
                



def longer( G, s, t ):
    tab = BFS(G,s,t)
    print(tab)
    n = len(tab)

    for i in range(n-1):
        G[tab[i+1]].remove(tab[i])
        G[tab[i]].remove(tab[i+1])


        # print("usunięto: ", tab[i+1]," ",tab[i])
        lenght = BFS(G,s,t)
        # print(lenght)
        if(lenght == None):
            return (tab[i+1],tab[i])

        if(len(lenght) > n):
            return (tab[i+1],tab[i])
        G[tab[i+1]].append(tab[i])
        G[tab[i]].append(tab[i+1])

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
