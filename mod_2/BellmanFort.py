
def BellemanFord(Tab,start,maxVertex):

    n = len(Tab)
    distance = [float('inf') for i in range(maxVertex)]
    distance[start] = 0

    def relax(touple):
        nonlocal distance,Tab

        i = touple[0]
        j = touple[1]
        weight = touple[2]
        return min(distance[j] , distance[i] + weight)
            


    for i in range(maxVertex + 1):

        for j in range(n):

            distance[Tab[j][1]] = relax(Tab[j])


    print(distance)
# Graf 1 - prosty graf bez cykli ujemnych
edges1 = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -2),
    (2, 3, 3)
]

# Graf 2 - zawiera ujemną wagę, ale bez cyklu ujemnego
edges2 = [
    (0, 1, 1),
    (1, 2, -1),
    (2, 3, -1),
    (3, 0, 2)
]

# Graf 3 - zawiera cykl o ujemnej wadze (do wykrycia)
edges3 = [
    (0, 1, 1),
    (1, 2, -1),
    (2, 3, -1),
    (3, 1, -1)
]

# Graf 4 - większy graf z mieszaną wagą
edges4 = [
    (0, 1, 6),
    (0, 2, 7),
    (1, 2, 8),
    (1, 3, 5),
    (1, 4, -4),
    (2, 3, -3),
    (2, 4, 9),
    (3, 1, -2),
    (4, 0, 2),
    (4, 3, 7)
]

# Graf 5 - graf z izolowanym wierzchołkiem i krawędziami dodatnimi
edges5 = [
    (0, 1, 3),
    (1, 2, 4),
    (2, 3, 2)
    # Wierzchołek 4 jest izolowany
]



BellemanFord(edges4,0,5)