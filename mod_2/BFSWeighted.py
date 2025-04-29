

def BFSWeighted(Tab,i):

    I = 0
    q = []
    

    n = len(Tab)

    

    visited = [False for _ in range(n)]
    distance = [0 for _ in range(n)]
    q.append((0,i))


    while(q):
        
        # print(q)
        vertex,counter = q.pop(0)
        # print(I , (vertex) , counter)
        if(counter != 0):
            q.append((vertex,counter-1))
        else:
            adjacent = Tab[vertex]
            m = len(adjacent)
            visited[vertex] = True

            
            for j in range(m):
                if(visited[adjacent[j][0]] == False):
                    
                    distance[adjacent[j][0]] = adjacent[j][1] + distance[vertex]
                    q.append((adjacent[j][0],adjacent[j][1]))
            

    print(distance)
graph1 = [
    [(1, 1), (2, 4)],     # 0
    [(2, 2), (3, 6)],     # 1
    [(3, 3)],             # 2
    []                    # 3
]

# Graf 2 - cykl i różne ścieżki
graph2 = [
    [(1, 2), (2, 5)],     # 0
    [(2, 1)],             # 1
    [(0, 9), (3, 2)],     # 2
    [(4, 1)],             # 3
    []                    # 4
]

# Graf 3 - graf nieskierowany zapisany jako skierowany (obie strony)
graph3 = [
    [(1, 10), (2, 3)],    # 0
    [(0, 10), (3, 2)],    # 1
    [(0, 3), (3, 8), (4, 2)],  # 2
    [(1, 2), (2, 8), (4, 7)],  # 3
    [(2, 2), (3, 7)]      # 4
]

# Graf 4 - większy, bardziej rozgałęziony
graph4 = [
    [(1, 7), (2, 9), (5, 14)], # 0
    [(2, 10), (3, 15)],        # 1
    [(3, 11), (5, 2)],         # 2
    [(4, 6)],                  # 3
    [(5, 9)],                  # 4
    []                         # 5
]

# Graf 5 - z "pułapką" (niskie wagi prowadzące do ślepego zaułka)
graph5 = [
    [(1, 1), (2, 10)],         # 0
    [(3, 1)],                  # 1
    [(3, 1)],                  # 2
    [(4, 1)],                  # 3
    []                         # 4
]
BFSWeighted(graph2,0)