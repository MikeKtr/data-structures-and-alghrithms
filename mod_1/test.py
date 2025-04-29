def partition(A,p,r):
    i = p-1
    j = r+ 1
    piwot = A[(p+r)//2]
    while(True):
        i+=1
        while(A[i] < piwot):
            i+=1

        j-=1
        while(A[j] > piwot):
            j-=1
        
        if(i >= j):
            return j
    
        A[j],A[i] = A[i],A[j]


def quicksort(A,p,r):
    if(p<r):
        q = partition(A,p,r)
        quicksort(A,p,q)
        quicksort(A,q+1,r)


tab = [15, 75, 41, 2, 25, 16, 77, 72, 37, 14, 62, 67, 93, 25, 87]
quicksort(tab,0,len(tab)-1)
print(tab)