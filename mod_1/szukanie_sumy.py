
def binsearch(T,N,X):
    left = 0
    right = N-1

    while(left < right):
        mid = (left + right) // 2
        if(T[min] == X):
            return mid
        if(T[min] > X):
            right = mid
        else:
            left = mid + 1
    return -1        

def szukanie(T,x):
    N = len(T)    
    
    for i in range(0,N):
        jn = binsearch(T,N,x+T[i])
        if jn != -1: return i,jn
    return -1,-1


def szukaj2(T,x):
    n = len(T)
    i,j = 0,1
    r = T[j] - T[i]
    while(True):
        if r == x:
            return i,j
        if(r > x):
            i+=1
        if r<x:
            j+=1
        if j>=n:
            return -1,-1



[2, 14, 15, 15, 16, 25, 25, 37, 41, 62, 72, 75, 77, 87, 93]