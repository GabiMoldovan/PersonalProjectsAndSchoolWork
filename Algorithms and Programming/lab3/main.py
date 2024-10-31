import math

def perfect_square(nr: int):
    '''
    Determina daca nr este patrat perfect
    :param nr: nr natyral
    :return: True daca nr este patrat perfect, altfel False
    '''
    if int(math.sqrt(nr)) == float(math.sqrt(nr)):
        return True
    return False

def verify_all_are_perfect_squares(lst: list[int]) -> bool:
    '''
    Parcurge toate numerele din lst si verifica prin functia perfect_square daca sunt patrate perfecte
    :param lst: o  lista de numere
    :return: True daca toate sunt patrate perfecte, altfel False
    '''
    for nr in lst:
        if perfect_square(int(nr)) == False:
            return False
    return True

def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de patrate perfecte
    :param lst: o lista de numere
    :return: Cea mai lunga subsecventa de patrate perfecte
    '''
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if verify_all_are_perfect_squares(lst[i:j + 1]) and len(lst[i:j + 1]) > len(result):
                result = lst[i:j + 1]
    return result

def bit_counts(x: int):
    '''
    Determina numarul de biti de 1 din reprezentarea binara a lui x
    :param x: nr natural
    :return: Numarul de biti de 1 din reprezentarea binara a lui x
    '''
    bits = int(0)
    while x:
        if x % 2 == 1:
            bits = bits + 1
        x = x // 2
    return bits

def verify_all_same_bit_counts(lst: list[int]) -> bool:
    '''
    Verifica daca toate numerele din lst au acelasi numar de biti de 1 folosind functia bit_counts
    :param lst: o lista de numere
    :return: True daca toate numerele au acelasi numar de biti de 1 in reprezentarea binara, altfel False
    '''
    bits = bit_counts(lst[0])
    for i in range(1, len(lst)):
        if bit_counts(lst[i]) != bits:
            return False
    return True

def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de numere care au acelasi numar de biti de 1 in reprezentarea binara
    :param lst: O lista de numere
    :return: Cea mai lunga subsecventa de numere care au acelasi numar de biti de 1 in reprezentarea binara
    '''
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if verify_all_same_bit_counts(lst[i:j + 1]) and len(lst[i:j + 1]) > len(result):
                result = lst[i:j + 1]
    return result

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

def verify_all_are_prime(lst: list[int]) -> bool:
    '''
    Determina daca toate numerele dintr-o lista sunt prime
    :param lst: o lista de numere
    :return: True daca toate sunt prime, False altfel
    '''
    for nr in lst:
        if is_prime(nr) == False:
            return False
    return True

def get_longest_all_primes(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de numere prime dintr-o lista de numere
    :param lst: O lista de numere
    :return: Cea mai lunga subsecventa de numere prime
    '''
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if verify_all_are_prime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(result):
                result = lst[i:j + 1]
    return result

def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([1,2,3,4,5]) == [1]
    assert get_longest_all_perfect_squares([1,4,9,3,7,4,9,16,25]) == [4,9,16,25]
    assert get_longest_all_perfect_squares([2,3,5,6,7,8]) == []

def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([2, 4, 6, 7, 6, 8, 8, 3, 6, 10]) == [3, 6, 10]
    assert get_longest_same_bit_counts([35, 85, 69, 36, 85, 85, 45]) == [85, 85, 45]
    assert get_longest_same_bit_counts([]) == []

def test_get_longest_all_primes():
    assert get_longest_all_primes([1,2,3,4,5]) == [2,3]
    assert get_longest_all_primes([1,6,2,3,5,7,11]) == [2,3,5,7,11]
    assert get_longest_all_primes([6,9,10,7,6,49,56]) == [7]

def main():
    while True:
        print("Optiuni:")
        print("1. Citeste o lista de numere de la tastatura")
        print("2. Determina cea mai lunga subsecventa cu toate elementele patrate perfecte")
        print("3. Determina cea mai lunga subsecventa cu toate elementele care au acelasi numar de biti 1 in reprezentarea binara")
        print("4. Determina cea mai lunga subsecventa cu toate elementele numere prime")
        print("5. Termina programul")
        option = input("Scrie numarul aferent optiunii: ")

        if option == "1":
            n = input("Dati numarul de numere: ")
            print("Dati numerele:", end = " ")
            lst = list(map(int, input().split()))

        if option == "2":
            print("Cea mai lunga subsecventa cu toate numerele patrate perfecte este:", end = " ")
            print(get_longest_all_perfect_squares(lst))

        if option == "3":
            print("Cea mai lunga subsecventa cu toate elementele care au acelasi numar de biti 1 in reprezentarea binara este:" , end = " ")
            print(get_longest_same_bit_counts(lst))

        if option == "4":
            print("Cea mai lunga subsecventa in care toate elementele sunt numere prime este:", end = " ")
            print(get_longest_all_primes(lst))

        if option == "5":
            break
        print()

if __name__ == '__main__':

    test_get_longest_all_perfect_squares()
    test_get_longest_same_bit_counts()

    main()
    exit(0)