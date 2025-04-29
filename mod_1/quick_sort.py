def Lomuto_partition(A,p,r):
    i = p-1
    piwot = A[r]
    
    for j in range(p,r):
        if(A[j] <= piwot):
            i+=1
            A[i],A[j] = A[j],A[i]

    A[r],A[i+1] = A[i+1],A[r]
    return i

def Hoare_partition(A,p,r):
    i = p - 1
    j = r + 1
    piwot = A[(p+r) // 2]
    while(True):
        i+=1
        
        while(A[i] < piwot):
            i+=1

        j-=1
        while(A[j] > piwot):
            j-=1

        if(i >= j):
            return j
        A[i],A[j] = A[j],A[i]


def quick_sort(A,p,r):

    if p < r:
        q = Hoare_partition(A,p,r)

#IMPORTANT INFO!: if you are using Lomuto_partition you can change line below to quick_sort(A,p,q-1) for faster sorting

        quick_sort(A,p,q)
        quick_sort(A,q+1,r)


def quick_sort_2(T,l,r):
    stos = [(l,r)]
    while stos:
        l,r = stos.pop()
        while l < r:
            q = Hoare_partition(T,l,r)
            if q - l < r - q:
                stos.append((q+1,r))
                r = q-1
            else:
                stos.append((l,q-1))
                l = q+1
tab = [15, 75, 41, 2, 25, 16, 77, 72, 37, 14, 62, 67, 93, 25, 87]
print(tab)
quick_sort(tab,0,4)
print(tab)