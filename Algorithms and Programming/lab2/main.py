def get_goldbach(n):
    '''
    Determina modalitatea de scriere a lui n ca suma de doua numere prime
    :param n: nr natural
    :return: doua numere p1, p2 ( ambele prime ) cu proprietatea ca n = p1 + p2
    '''
    # Pentru a avea o solutie, parametrul dat trebuie sa respecte conditiile: n > 3 si n % 2 == 0 ( sa fie par )
    for i in range(int(n), 1, -1):
        if prime(i):
            for j in range(3, int(i)+1, 2):
                if prime(j) and int(i)+int(j)==int(n):
                    return i, j
    return -1, -1

def prime(n):
    '''
    Determina primalitatea lui n
    :param n: nr natural
    :return: True daca n este prim, altfel False
    '''
    if int(n) < 2: return False
    for i in range(2, int(n) // 2 + 1):
        if int(n) % int(i) == 0: return False
    return True

def test_get_goldbach():
    assert get_goldbach(6) == (3, 3)
    assert get_goldbach(7) == (-1, -1)
    assert get_goldbach(256) == (251, 5)

def test_x0(root, x, x0):
    if float(abs(float(root) - float(x))) < float(x0):
        return True
    return False

def get_newton_sqrt(n, steps):
    '''
    Calculeaza radical din n folosind steps pasi
    Pentru un rezultat cat mai aproape de sqrt(n), se seteaza x0 sa fie cat mai mic ( ex: 0.000001 )
    :param n: nr natural
    :param steps: nr natural
    :return: sqrt(n)
    '''
    x=n
    x0=2
    while steps:
        steps=int(steps)-1
        root=float(0.5)*(float(x)+float(n)/float(x))
        if test_x0(root, x, x0) == True:
            break
        x=float(root)
    return float(root)

def test_get_newton_sqrt():
    assert get_newton_sqrt(100, 10) == 10.032578510960604
    assert get_newton_sqrt(6, 3) == 2.607142857142857


def test_is_palindrome():
    assert is_palindrome(252) == True
    assert is_palindrome(123454321) == True
    assert is_palindrome(135521) == False


def is_palindrome(n):
    '''
    Determina daca n este palindrom ( palindrom, adica oglinditul numarului este egal cu numarul initial )
    :param n: nr natural
    :return: True daca este palindrom, altfel False
    '''
    aux = int(n)
    ogl = int(0)
    while n:
        ogl = ogl * int(10) + int(n) % int(10)
        n = int(n) // int(10)
    if aux == ogl:
        return True
    return False

def main():
    while True:
        print("Optiuni:")
        print("1. Conjunctura lui Goldbach")
        print("2. Calcularea radicalului folosind metoda lui Newton")
        print("3. Verifica daca un numar este palindrom")
        print("4. Termina programul")
        option = input("Scrie numarul aferent optiunii: ")

        if option == "1":
            n = input("Introdu numarul: ")
            p1, p2 = get_goldbach(n)
            if p1 == -1:
                print("NU SE VERIFICA!")
            else:
                print(str(n) + " = " + str(p1) + " + " + str(p2))

        if option == "2":
            n = input("Introdu numarul: ")
            steps = input("Introdu numarul de pasi: ")
            print("Solutia este:", end=" ")
            print(get_newton_sqrt(n, steps))

        if option == "3":
            n = input("Introdu numarul: ")
            print("Valoarea de adevar a propozitiei \" " + str(n) + " este palindrom \", este:", end=" ")
            print(is_palindrome(n))

        if option == "4":
            break
        print()

if __name__ == '__main__':

    test_get_newton_sqrt()
    test_get_goldbach()
    test_is_palindrome()

    main()
    exit(0)