from zad1testy import runtests

T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]

def merge(left,right):
    
    if left == None:
        return right
    if right == None:
        return left

    res = ["" for i in range(len(left) + len(right))]

    i,j = 0,0

    

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res[i+j] =left[i]
            i+=1
        else:
            res[i+j] = right[j]
            j+=1

    while(j < len(right)):
        res[i+j] = right[j]
        j+=1

    while(i < len(left)):
        res[i+j] = left[i]
        i+=1
    
    return res

def merge_sort(T):
    if len(T) <= 1:
        return T

    mid = len(T) // 2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return merge(left,right)

def sort(s):
    return min(s,s[::-1])

def max_string(T):
    maxs = 0
    for i in T:
        if(len(i) > maxs):
            maxs = len(i)

    return maxs

def countingSort(T,i,n):
    ResArr = [[] for i in range(27)]
    for j in range(n):
        letter = T[j][i:i+1] 
        
        ResArr[ord(letter) - 96 if letter  != "" else 26].append(T[j])
    
    T = []

    for j in ResArr:
        T = T + j
    
    return T

def strong_string(T):
    maxs = max_string(T)

    n = len(T)

    for i in range(n-1,-1,-1):
        T[i] = sort(T[i])



    if(maxs > 50000):
        
        T = merge_sort(T) 
    else:
        
        for i in range(maxs):
            T = countingSort(T,i,n)

    

    maxw = 1
    curr = 1
    for i in range(1,n):
        if(T[i-1] == T[i]):
            curr +=1 
        else:
            
            maxw = max(maxw,curr)
            curr = 1
        maxw = max(maxw,curr)
    return maxw
# Odkomentuj by uruchomic duze testy
runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
#runtests( strong_string, all_tests=False )

strong_string(T)