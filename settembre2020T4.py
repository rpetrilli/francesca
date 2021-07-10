class stazione():
    def __init__(self):
        pass

    def set_targa(self,targa):
        self.__targa=targa
    def set_denominazione(self,denominazione):
        self.__denominazione=denominazione
    def set_tipo_locomotiva(self,tipo_locomotiva):
        self.__tipo_locomotiva=tipo_locomotiva
    def set_hh(self,hh):
        self.__hh=hh
    def set_mm(self,mm):
        self.__mm=mm
    def set_num_passeggeri(self,num_passeggeri):
        self.__num_passeggeri=num_passeggeri
    def get_targa(self):
        return self.__targa
    def get_denominazione(self):
        return self.__denominazione
    def get_tipo_locomotiva(self):
        return self.__tipo_locomotiva
    def get_hh(self):
        return self.__hh
    def get_mm(self):
        return self.__mm
    def get_num_passeggeri(self):
        return self.__num_passeggeri
    def __str__(self):
        return 'targa: '+ self.__targa + ' numero passeggeri: '+ str(self.__num_passeggeri)

    def carica(self):
        self.__targa=input('inserire targa: ')
        self.__denominazione=input('inserire denominazione: ')
        self.__tipo_locomotiva=input('inserire tipo locommotiva: ')
        self.__hh=int(input('inserire ore: '))
        self.__mm=int(input('inserire minuti: '))
        self.__num_passeggeri=int(input('inserire numero passeggeri: '))

    def __gt__(self, other):
        return self.__hh * 60 + self.__mm > other.__hh * 60 + other.__mm



def main():
    n=2
    lista_treni=carica(n)
    print_elenco(lista_treni)
    lista_ordinata = ordinamento(lista_treni)
    print_elenco(lista_ordinata)
    print ("numero medio passeggeri %f " % media(lista_ordinata, 2))

def carica(n):
    elenco_treni = []
    for i in range(n):
        treno = stazione()
        treno.carica()
        elenco_treni.append(treno)

    return elenco_treni


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

def media(lista_ordinata, nr):
    sum = 0
    for item in lista_ordinata[:nr]:
        sum = sum + item.get_num_passeggeri()

    media = 1.0 * sum / nr
    return media




main()

