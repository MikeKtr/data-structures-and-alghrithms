def wyb(tab):
    n = len(tab)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if(tab[j] < tab[min]):
                min = j
        (tab[i],tab[min]) = (tab[min],tab[i])
    print(tab)

tab = [15, 75, 41, 2, 25, 16, 77, 72, 37, 14, 62, 15, 93, 25, 87]
wyb(tab)

#liczba porównań: (1+n) / 2 * n 

#liczba przypisań : n^2 + 2n

