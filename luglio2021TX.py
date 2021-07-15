
class Reperto():
    __id_reperto = None
    __luogo_ritrov = None
    __anno_ritrov = None
    __mese_ritrovamento = None
    __peso = None

    def get_id_reperto(self):
        return self.__id_reperto

    def get_luogo_ritrov(self):
        return self.__luogo_ritrov

    def get_anno_ritrov(self):
        return self.__anno_ritrov

    def get_mese_ritrovamento(self):
        return self.__mese_ritrovamento

    def get_peso(self):
        return self.__peso

    def set_id_reperto(self, id_reperto):
        self.__id_reperto = id_reperto

    def set_luogo_ritrov(self, luogo_ritrov):
        self.__luogo_ritrov = luogo_ritrov

    def set_anno_ritrov(self, anno_ritrov):
        self.__anno_ritrov = anno_ritrov

    def set_mese_ritrovamento(self, mese_ritrovamento):
        self.__mese_ritrovamento = mese_ritrovamento

    def set_peso(self, peso):
        self.__peso = peso

    def carica(self):
        self.__id_reperto = input('inserire id reperto: ')
        self.__luogo_ritrov = input('inserire luogo ritrovamento: ')
        self.__anno_ritrov = int(input('inserire Anno ritrovamento: '))
        self.__mese_ritrovamento = int(input('inserire mese ritrovamento: '))
        self.__peso = int(input('inserire peso: '))

    def __gt__(self, other):
        #in questo modo l'ordinamento è descrescente
        return self.__peso < other.__peso

    def __str__(self):
        return 'Cod:  ' +  self.get_id_reperto()  + ' Luogo: ' + self.get_luogo_ritrov() + \
               ' Ritrovamento:' + str(self.get_anno_ritrov()) + ' ' + str(self.get_mese_ritrovamento()) + \
               ' peso:' + str(self.get_peso())


    def get_mesi(self):
        return self.__anno_ritrov * 12 + self.__mese_ritrovamento

    def is_valido(self):
        #Restituisce False se __id_reparto non è valorizzato o se l'anno di ritrovamento non è valido
        return not (self.__id_reperto is None or self.__anno_ritrov >= 1945);




def main():
    n = 3000
    lista_reperti = caricaLista(n)
    antico(lista_reperti)

    reperti_pompei = filtra_per_luogo(lista_reperti, 'Pompei')
    reperti_ordinati = ordinamento(reperti_pompei)
    print_elenco(reperti_ordinati)

def antico(lista_reperti):
    reperto = None
    #scrorro la lista dei reperti saltando quelli non del XIV secolo
    #e prendo il più antico
    for item in lista_reperti:
        #il reperto non è del XIV secolo
        if item.get_anno_ritrov() < 1300 or item.get_anno_ritrov() > 1399:
            continue
        if reperto is None:
            reperto = item
        elif item.get_mesi() < reperto.get_mesi():
            reperto = item

    if reperto is not None:
        print(item)
    else:
        print ('Nessun reperto appartenente al XIV secolo in archivio')

def caricaLista(n):
    elenco = []
    for i in range(n):
        item = Reperto()
        # Chiede di inserire nuovamente il record fino a quando non viene
        # inserito un record valido
        while not item.is_valido():
            item.carica()

        elenco.append(item)

    return elenco

def filtra_per_luogo(lista_reperti, luogo):
    lista_filtrata = []
    for item in lista_reperti:
        if item.get_luogo_ritrov() == luogo:
            lista_filtrata.append(item)

    return lista_filtrata


def print_elenco(elenco):
    for i in range(len(elenco)):
        print(str(elenco[i]))

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

main()