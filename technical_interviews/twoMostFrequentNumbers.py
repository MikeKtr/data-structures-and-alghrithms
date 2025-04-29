f = open('data.txt','r')
tab = f.readlines()


n = len(tab)

liczby = {}

for i in range(n):
    if(tab[i] in liczby):
        liczby[tab[i]] += 1
    else:
        liczby[tab[i]] = 1

top_two = sorted(liczby.items(), key=lambda x: x[1], reverse=True)[:2]


print(top_two)
