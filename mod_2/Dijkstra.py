import heapq


def Dijkstra(G,s,k):

    n = len(G)

    visited = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]


    distance[s] = 0
    q = []
    heapq.heappush(q,(1,s))

    while(q):
        priority,index = heapq.heappop(q)

        adjacent = G[index]
        m = len(adjacent)

        visited[index] = True
        for j in range(m):
            if(visited[adjacent[j][0]] == False):
                print("not visited")
                print("wieszchołek" , index, adjacent[j][0])
                print(distance[adjacent[j][0]],adjacent[j][1],distance[index])
                print()
                distance[adjacent[j][0]] = min(distance[adjacent[j][0]],adjacent[j][1] + distance[index])
                heapq.heappush(q,(distance[adjacent[j][0]],adjacent[j][0]))
                
            else:
                print("visited")
                print("wieszchołek: " , index , adjacent[j][0])
                print(distance[adjacent[j][0]],distance[index],adjacent[j][1])
                print()
                distance[adjacent[j][0]] = min(distance[adjacent[j][0]],distance[index]+adjacent[j][1])


    

    print(distance)
    print(distance[k])

graph5 = [
    [(1, 1), (2, 10)],         # 0
    [(3, 1)],                  # 1
    [(3, 1)],                  # 2
    [(4, 1)],                  # 3
    []                         # 4
]
Dijkstra(graph5,0,2)