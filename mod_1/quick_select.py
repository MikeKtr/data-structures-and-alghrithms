#given the array A, return value that would be on index k after sorting


def quick_select(A,p,r,k):
    i = p-1
    
    piwot = A[k]
    A[k],A[r] = A[r],A[k]

    for j in range(p,r):
        if(A[j] <= piwot):
            i+=1
            A[i],A[j] = A[j],A[i]
    A[r],A[i+1] = A[i+1],A[r]
    
    if(i+1 == k):
        return A[k]
    elif(i+1 < k):
        return quick_select(A,i+1,r,k)
    else:
        return quick_select(A,p,i,k)


tab = [15, 75, 41, 2, 25, 16, 77, 72, 37, 14, 62, 67, 93, 25, 87]
print(quick_select(tab,0,5,2))