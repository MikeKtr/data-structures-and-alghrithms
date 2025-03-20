A=[2,3,9,2,5,1,3,7,10] 

B=[2,1,3,4,3,10,6,6,1,7,10,10,10] 

def sito_eratostenesa(n):
    pierwsze = [True for i in range(n+1)]
    pierwsze[0] = pierwsze[1] = False
    p = 2
    while (p * p <= n):
        if (pierwsze[p] == True):
            for i in range(p * p, n+1, p):
                pierwsze[i] = False
        p += 1
    return pierwsze

# C=[2,9,2,5,7,10]

def sito(n):
    tab = [1 for i in range(n+1)]
    tab[0] = tab[1] = 0
    i = 2
    while(i * i<= n):
        if(tab[i] == 1):
            for i in range(i*i,n+1,i):
                tab[i] = 0
        i += 1
    return tab

maxi = max(B)

map = [0 for i in range(maxi)]
sito = sito(maxi)


for i in range(len(B)):
    map[B[i]-1] += 1

C = []
j = 0

for i in range(len(A)):

    if(sito[map[A[i]-1]] == 0):
        C.append(A[i])
print(C)