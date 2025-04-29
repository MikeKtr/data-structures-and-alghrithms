from zad5testy import runtests
import heapq

def Dijkstra(Tab,a):

    n = len(Tab)

    visited = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    q = []
    distance[a] = 0
    heapq.heappush(q,(0,a))

    while(q):
        priority,index = heapq.heappop(q)
        adjacent = Tab[index]

        m = len(adjacent)
        visited[index] = True
        for j in range(m):
            distance[adjacent[j][0]] = min(distance[adjacent[j][0]],distance[index] + adjacent[j][1])
            if(visited[adjacent[j][0]] == False):
                heapq.heappush(q,(distance[adjacent[j][0]],adjacent[j][0]))

    # print(distance)
    return distance




def spacetravel( n, E, S, a, b ):

    Tab = [[] for _ in range(n)]

    for i,j,k in E:
        Tab[i].append((j,k))
        Tab[j].append((i,k))
    

    distanceFromA = Dijkstra(Tab,a)
    distanceFromB = Dijkstra(Tab,b)

    minWormholeFromA = float('inf')
    minWormholeFromB = float('inf')

    for i in S:
        minWormholeFromA = min(minWormholeFromA,distanceFromA[i])
        minWormholeFromB = min(minWormholeFromB,distanceFromB[i])


    # print(minWormholeFromA)
    # print(minWormholeFromB)
    res = min(distanceFromA[b],minWormholeFromA + minWormholeFromB)
    if res != float('inf'):
        return res

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )

