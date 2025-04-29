import heapq


def dijkstra(Tab,i):

    n = len(Tab)


    distance = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    distance[i] = 0
    q = []
    heapq.heappush(q,(0,i))

    while(q):
        weight,index = heapq.heappop(q)
        
        adjacent = Tab[index]

        m = len(adjacent)

        visited[index] = True

        for j in range(m):

            distance[adjacent[j][0]] = min(distance[adjacent[j][0]] , distance[index] + adjacent[j][1])

            if(visited[adjacent[j][0]] == False):
                heapq.heappush(q,(distance[adjacent[j][0]] , adjacent[j][0]))



    print(distance)


# Graf 1 - prosty, 4 wierzchołki, bez cykli
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
dijkstra(graph2,0)