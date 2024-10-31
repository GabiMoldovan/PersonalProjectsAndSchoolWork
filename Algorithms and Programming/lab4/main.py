def determina_negative(lst: list[int]):
    '''
    Afiseaza numerele negative nenule din lst
    :param lst: o lista de numere
    :return: None daca nu exista numere negative, altfel 1
    '''
    rez = []
    for nr in lst:
        if nr<0:
            rez.append(nr)
    return rez

def det_cmm_nr_cu_cifra_citita(lst: list[int], cifracit: int):
    '''
    Calculeaza cel mai mic numar din lst care are ultima cifra egala cu cifracit
    :param lst: lista de numere
    :param cifracit: cifra citita de la tastatura
    :return: cel mai mic numar din lst care are ultima cifra egala cu cifracit
    '''
    rez = -1
    for nr in lst:
        if int(nr) % int(10) == cifracit:
            rez=nr
            break
    for nr in lst:
        if int(nr) % int(10) == cifracit and int(nr) < int(rez):
            rez = nr
    return rez

def is_prime(n) -> bool:
    '''
    Determina primalitatea lui n
    :param n: nr natural
    :return: True daca n este prim, altfel False
    '''
    if int(n) < 2:
        return False
    for i in range(2, int(n) // 2 + 1):
        if int(n) % int(i) == 0: return False
    return True

def is_superprime(nr: int) -> bool:
    '''
    Verifica daca nr este superprim
    :param nr: numarul verificat
    :return: True daca este superprim, False altfel
    '''
    while nr:
        if is_prime(nr) == False:
            return False
        nr = nr // 10
    return True

def get_all_superprimes(lst: list[int]):
    '''
    Calculeaza si returneaza lista de numere superprime din lst
    :param lst: o lista de numere
    :return: numerele superprime din lst
    '''
    rez = []
    for nr in lst:
        if is_superprime(nr) == True:
            rez.append(nr)
    return rez

def cmmdc(nr1: int, nr2: int):
    '''
    Calculeaza cmmdc a doua nr
    :param nr1:  primul nr
    :param nr2: al doilea nr
    :return: cmmdc al celor doua numere
    '''
    if nr2==0:
        return nr1
    return cmmdc(nr2, nr1%nr2)

def get_cmmdc(lst: list[int]):
    '''
    Calculeaza cmmdc-ul numerelor pozitive si nenule din lst
    :param lst: o lista
    :return: cmmdc-ul numerelor pozitive din lst
    '''
    rez=0
    for i in range(0, len(lst)):
        if lst[i]>0:
            rez=lst[i]
            for j in range(i,len(lst)):
                rez=cmmdc(rez,lst[j])
    return rez


def get_invers(nr: int):
    '''
    calculeaza inversul unui numar negativ
    :param nr: numarul negativ
    :return: inversul lui nr
    '''
    nr = nr * (-1)
    oglindit = 0
    while nr:
        oglindit = oglindit*10 + nr % 10
        nr = nr // 10
    return oglindit*(-1)

def modifica_lista_cmmdc_ord_inversa(lst: list[int]):
    '''
    Genereaza o noua lista pe baza lst in care numerele pozitive si nenule se inlocuiesc cu cmmdc-ul lor
    iar numerele negative cu cifrele in ordine inversa
    :param lst: o lista
    :return: Noua lista dupa aplicarea modificarilor
    '''
    rez = []
    cmmdc = get_cmmdc(lst)
    for nr in lst:
        if nr == 0:
            rez.append(0)
        elif nr > 0:
            rez.append(cmmdc)
        else:
            rez.append(get_invers(nr))
    return rez

def execute_tests():
    '''
    Ruleaza functiile de test assert
    :return:None
    '''
    assert determina_negative([-1,-2,5]) == [-1,-2]
    assert determina_negative([-5, -7, 0, 1]) == [-5,-7]
    assert determina_negative([0]) == []

    assert det_cmm_nr_cu_cifra_citita([16, 36, 4], 6) == 16
    assert det_cmm_nr_cu_cifra_citita([10,25,55,65], 5) == 25
    assert det_cmm_nr_cu_cifra_citita([-1, -10, 27, 77], 7) == 27

    assert get_all_superprimes([23, 68]) == [23]
    assert get_all_superprimes([]) == []

    assert modifica_lista_cmmdc_ord_inversa([-76, 12, 24, -13, 144]) == [-67, 144, 144, -31, 144]
    assert modifica_lista_cmmdc_ord_inversa([-13, -63, -745]) == [-31, -36, -547]
    assert modifica_lista_cmmdc_ord_inversa([]) == []
    pass

def main():
    lst = []
    n = 0
    while True:
        print("Optiunile sunt:")
        print("0. Afisarea numerelor care se afla in lista actuala.")
        print("1. Citeste o lista de numere (se suprascrie lista veche).")
        print("2. Afisarea tuturor numerelor negative din lista.")
        print("3. Afisarea celui mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura.")
        print("4. Afisarea tuturor numerelor din lista care sunt superprime.")
        print("5. Afisarea listei obtinute din lista initiala in care numerele pozitive si nenule au fost inlocuite cu \
CMMDC-ul lor si numerele negative au cifrele in ordine inversa.")
        print("6. Inchide programul")
        optiune = input("Selecteaza numarul aferent optiunii: ")

        if optiune == "0":
            if len(lst) == 0:
                print("Lista este goala! Cititi o lista de numere")
            else:
                print("Lista este:", end = " ")
                for nr in lst:
                    print(len(nr), end=" ")

        elif optiune == "1":
            n = input("Dati numarul de numere: ")
            print("Dati numerele:", end=" ")
            lst = list(map(int, input().split()))

        elif optiune == "2":
            rez = []
            rez = determina_negative(lst)
            if len(rez) == 0:
                print("Nu exista numere negative nenule.")
            else:
                print("Numerele negative nenule din lista sunt:", end = " ")
                for nr in rez:
                    print(nr, end=" ")

        elif optiune == "3":
            cifracit = int(input("Dati cifra: "))
            rez = det_cmm_nr_cu_cifra_citita(lst, cifracit)
            if rez == -1:
                print("Nu exista niciun numar care sa respecte conditia.")
            else:
                print("Numarul este: " + str(rez))
            # testare pentru numere cu o cifra

        elif optiune == "4":
            rez = []
            rez = get_all_superprimes(lst)
            if len(lst) == 0:
                print("Nu exista numere superprime in lista")
            else:
                print("Numerele superprime sunt:", end = " ")
                for nr in rez:
                    print(nr, end = " ")

        elif optiune == "5":
            lista_modificata = []
            lista_modificata = modifica_lista_cmmdc_ord_inversa(lst)
            print("Lista modificata este:", end = " ")
            for nr in lista_modificata:
                print(nr, end=" ")
        elif optiune == "6":
            break
        else:
            print("Optiune invalida! Scrieti un numar valid unei optiuni")
        print()

if __name__ == '__main__':

    # apelarea functiilor de test
    execute_tests()

    main()

    exit(0)