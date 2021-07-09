
R = int(input("Inserire il numero di righe:"))
C = int(input("Inserire il numero di colonne:"))

if R < 8 or R > 35 or C < 8 or C > 35:
    raise ValueError("Le dimensioni della matrice devono essere comprese fra 8 e 35")

matrix = []
print("Inserire gli elementi della matrice per riga:")

# For user input
for i in range(R):
    a = []
    for j in range(C):
        val = int(input())

        a.append(val)
    matrix.append(a)

#Visualizzazione della matrice caricata
print("Matrice caricata:")
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

#Inserimento del vettore
print("Inserire gli elementi del vettore:")
vector = []
for i in range(C):
    vector.append(int(input()))

print("Vettore inserito:")
for i in range(C):
    print(vector[i])

#Effettua il prodotto matrice vettore
result = []
for j in range(R):
    element = 0;
    for i in range(C):
        element += matrix[j][i] * vector[j]
    result.append(element)

print("Rilsultato inserito:")
for i in range(R):
    print(result[i])

#Ordinamento dei valori nel vettore risultante
duplicatedResult = result[:]
for iter_num in range(len(duplicatedResult) - 1, 0, -1):
    for idx in range(iter_num):
        if list[duplicatedResult] > duplicatedResult[idx + 1]:
            temp = duplicatedResult[idx]
            duplicatedResult[idx] = duplicatedResult[idx + 1]
            duplicatedResult[idx + 1] = temp

nrGraters = 0
for item in duplicatedResult:
    if item > 30:
        nrGraters = nrGraters+1

print ("Percentuale di valori maggiorni di 30 nel vettore risultato: ")
print ( 100.0 * nrGraters / len(duplicatedResult))