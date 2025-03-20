#   you set two pointers to begining and end of array
#   if values of those pointers is greater than value we are looking for, you move pointer from begining to the right
#   in other case you move pointer from end to the left


def two_sum(tab,n):
    i,j = 0,len(tab)-1
    while(tab[i] + tab[j] != n and i <= j):
        if(tab[i] + tab[j] < n):
            i+=1
        else:
            j-=1
    return i,j

tab = [2, 14, 15, 16, 25, 26, 37, 41, 62, 67, 72, 75, 77, 87, 93]
print(two_sum(tab,100))
