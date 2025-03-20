#merge sort is a sorting algorithm that rely on recursion.

#you split it in half until you have only one element in two arrays, then you connect them based on which is biger

def merge_sort(tab,left,right):

    #break condition

    if(right - left < 1):
        return tab[left:right+1]

    #calculating mid
    mid = left + (right - left)//2

    #using recursion, program is calling merge_sort two times, one with left half and secont time with right half
    tab1 = merge_sort(tab,left,mid)
    tab2 = merge_sort(tab,mid+1,right) 
    
    #after sorting both halfes separatly, you merge them together by comparing elements with each other
    return merge(tab1,tab2)


def merge(tab1,tab2):
    n,m = len(tab1),len(tab2)
    res = [0] * (n+m)
    i,j = 0,0

    # if first element from tab1 is smaller than first element from tab2 algorightm places it on first position
    #then it compares second element from tab1 and still first element from tab1
    #and so on, until it reaches end of eather tab1 or tab2
    #then it adds elements that remained unsigned and adds them to end of result array
    while(i < n and j < m):
        if(tab1[i] < tab2[j]):
            res[i+j] = tab1[i]
            i+=1
        else:
            res[i+j] = tab2[j]
            j+=1
    while(j < m):
        res[i+j] = tab2[j]
        j+=1

    while(i < n):
        res[i+j] = tab1[i]
        i+=1
    return res
    



tab = [15, 75, 41, 2, 25, 16, 77, 72, 37, 14, 62, 67, 93, 25, 87]
print("Table before sorting: ")
print(tab)
print("Table after sorting")
print(merge_sort(tab,0,len(tab)-1))