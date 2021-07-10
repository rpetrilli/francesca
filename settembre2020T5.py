def main():
    R = int(input("Inserire il numero di righe:"))
    C = int(input("Inserire il numero di colonne:"))
    if R < 2 or R > 35 or C < 2 or C > 35:
        R = int(input("Inserire il numero di righe:"))
        C = int(input("Inserire il numero di colonne:"))
    matrix = leggiMatrice(R, C)
    print(matrix)
    vett = leggiVettore(C)
    print(vett)
    risultatoProd = calcProdotto(matrix, vett)
    print('risultato prodotto: ')
    print(risultatoProd)

    vetOrdinato = ordinamento(risultatoProd)
    print('Vettore ordinato: ')
    print(vetOrdinato)

    p = calcolaPercentuale(vetOrdinato, 2)
    print ('la percentuale è %f' % (p))

def leggiMatrice(R, C):
    matrix = []
    print("Inserire gli elementi della matrice per riga:")
    for i in range(R):
        a = []
        for j in range(C):
            val = int(input('inserire valore: '))
            a.append(val)
        matrix.append(a)
    return matrix



def leggiVettore(C):
    vettore = []
    for i in range(C):
        val = int(input('inserire valore del vettore: '))
        vettore.append(val)
    return vettore


def calcProdotto(matrix, vett):
    risultato = []
    R = len(matrix)
    C = len(vett)
    for i in range(R):
        p = 0
        for j in range(C):
            p = p + matrix[i][j] * vett[j]
        risultato.append(p)
    return risultato


def ordinamento(vettore):
    copia = vettore[:]
    n = len(copia)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if copia[j] > copia[j + 1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                already_sorted = False
        if already_sorted:
            break

    return copia


def calcolaPercentuale(vettore, nr):
    cnt = 0
    for item in vettore[-nr:]:
        if item > 30:
            cnt = cnt + 1
    return 100.0 * cnt / nr


main()