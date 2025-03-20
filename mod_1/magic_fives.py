#median of medians, in polish "Magic Fives"

def Hoare_partition(A,p,r,x):
    i = p - 1
    j = r + 1
    piwot = x
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



def magic_fives(A,p,r,k):
    print("A:" ,A[p:r], p , r)
    n = r+1
    B = []
    for i in range(r//5):
        # print((A, 5 * i  , 5 * (i+1) - 1,  5 * (i + 1) - 3))
        B.append(quick_select(A, 5 * i  , 5 * (i+1) - 1,  5 * (i + 1) - 3))
    if(n//5 != n/5):
        # print(A,n//5 * 5,n, ((n//5 * 5) + n)//2)
        B.append(quick_select(A,n//5 * 5,n - 1, ((n//5 * 5) + n)//2))
    
    print("B:" , B)
    m = len(B)
    res = quick_select(B,0,m-1,m//2)
    j = Hoare_partition(A,0,n-1,res)
    index = A.index(res)

    
    A[j],A[index] = A[index],A[j]

    if(k == index):
        return A[index]
    elif(k < index):
        return magic_fives(A,p,index-1,k)
    elif(k > index):
        return magic_fives(A,index+1,r,k)
    
    
    


tab = [15, 75, 41, 2, 25, 16, 77, 72, 37, 14, 62, 67, 93, 25, 87, 64, 56, 11]
print(magic_fives(tab,0,17,10))
