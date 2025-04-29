
class Node:
    def __init__(self,value):
        self.value = value
        self.parent = self
        self.rank = 0

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if(x == y):return
    if(x.rank > y.rank):
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def MST(A):
    A = sorted(A,key=lambda A: A[2]) 
    print(A)
    n = len(A)

    nodes = [Node(i) for i in range(n)]
    res = []
    



    for i in range(n):
        if(find(nodes[A[i][0]]) != find(nodes[A[i][1]])):
            union(nodes[A[i][0]],nodes[A[i][1]])
            res.append((A[i][0],A[i][1]))
        

    return res

edges2 = [
    (0, 1, 4),
    (1, 2, 6),
    (2, 0, 5),
    (2, 3, 2),
    (3, 0, 1)
]
print(MST(edges2))
        