from collections import deque

def BFS(graf):
    n = len(graf)
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    distance = [-1 for i in range(n)]
    result = []
    q = deque()

    visited[0] = True
    distance[0] = 0

    q.append(0)
    result.append(0)
    while q:
        
        index = q.popleft()

        i = graf[index]

        for j in range(len(i)):

            if visited[i[j]] == False:
                visited[i[j]] = True
                parent[i[j]] = i
                distance[i[j]] = distance[index] + 1
                q.append(i[j])
                result.append(i[j])
    print(result)
    print(distance)


graph = [
    [1, 2],  # sąsiedzi wierzchołka 0
    [3, 4],  # sąsiedzi wierzchołka 1
    [4],     # sąsiedzi wierzchołka 2
    [],      # 3 nie ma sąsiadów
    []       # 4 nie ma sąsiadów
]
BFS(graph)


