class Node:
    def __init__(self,value):
        self.parent = self
        self.value = value
        self.rank = 0

def find(x):
    if(x != x.parent):
        x.parent = find(x.parent)
    return x.parent

def union(x,y):

    x = find(x)
    y = find(y)

    if(x == y):
        return 0
    
    if(x.rank < y.rank):
        x.parent = y
    else:
        y.parent = x
        if(x.rank == y.rank):
            x.rank += 1




def MST(Tab):

    Tab = sorted(Tab,key = lambda  Tab:Tab[2])
    res = []
    n = len(Tab)

    maxVertex = max(Tab[i][1] for i in range(n))

    

    Nodes = [Node(i) for i in range(maxVertex + 1)]

    for i in range(n):
        
        x = find(Nodes[Tab[i][0]])
        y = find(Nodes[Tab[i][1]])

        if(x.parent != y.parent):
            union(Nodes[Tab[i][0]],Nodes[Tab[i][1]])
            res.append((Tab[i][0],Tab[i][1]))

    
    print(res)

    

edges3 = [
    (0, 1, 3),
    (1, 2, 1),
    (2, 3, 1),
    (3, 4, 6),
    (4, 5, 5),
    (5, 6, 2),
    (0, 6, 10),
    (1, 4, 8)
]
MST(edges3)