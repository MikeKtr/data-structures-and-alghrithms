from collections import deque

def BFS(graf,start,end):
    n = len(graf)
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    distance = [-1 for i in range(n)]
    result = []
    q = deque()

    visited[start] = True
    distance[start] = 0

    q.append(start)
    result.append(start)
    while q:
        
        index = q.popleft()

        i = graf[index]

        for j in range(len(i)):

            if visited[i[j]] == False:
                print(q)
                print(visited)
                visited[i[j]] = True
                parent[i[j]] = i
                distance[i[j]] = distance[index] + 1
                q.append(i[j])
                if i[j] == end:
                    return distance[i[j]]
    


graph = [
    [1, 2],         
    [0, 2, 3],     
    [0, 1, 4],      
    [1, 4, 5],      
    [2, 3, 5, 6],   
    [3, 4, 6],      
    [4, 5]          
]

print(BFS(graph,1,6))


