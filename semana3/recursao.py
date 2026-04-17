l = [1, 2, 3]


def imprime_rec(l, i=0):
    if i < len(l):
        print(l[i])
        imprime_rec(l, i+1)


imprime_rec(l)
