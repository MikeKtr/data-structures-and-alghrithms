from zad2testy import runtests

def merge(A,left,right,mid):
    total=0
    tab1 = A[left:mid+1]
    tab2 = A[mid+1:right+1]
    # print(tab1,tab2)
    m,n = len(tab1),len(tab2)
    i,j = 0,0

    while(i < m and j < n):
        if(tab1[i] <= tab2[j]):
            # print("index: ", left + i + j, " enquals: " , tab1[i])
            A[left + i+j] = tab1[i]
            i+=1
        else:
            # print("index: ", left + i + j, " enquals: " , tab2[j])
            A[left + i+j] = tab2[j]
            j+=1
            # print("added ", m + j - i  )
            total += m - i 

    while(i < m):
        A[left + i+j] = tab1[i]
        i+=1

    while(j < n):
        A[left + i+j] = tab2[j]
        j+=1

    # print(total)
    return total


def merge_sort(A,left,right):
    total = 0
    if left < right:
        mid = left + (right - left)//2

        total += merge_sort(A,left,mid)
        total += merge_sort(A,mid+1,right)
        total += merge(A,left,right,mid)
    
    return total



def count_inversions(A):
    res = merge_sort(A,0,len(A)-1)

    return res


A = [1, 20, 6, 4, 5]
# print(count_inversions(A))
# print(A)
# count_inversions(A)
# Odkomentuj by uruchomic duze testy
runtests( count_inversions, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
# runtests( count_inversions, all_tests=False )
