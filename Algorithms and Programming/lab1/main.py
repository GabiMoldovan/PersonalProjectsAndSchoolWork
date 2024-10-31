def is_prime(n):
    '''
    Checks if a number is prime
    :param n: natural number
    :return: True if prime, false else
    '''
    if int(n) < 2: return False
    for i in range(2, int(n)//2 + 1):
        if int(n)%int(i)==0: return False
    return True

def get_product(lst):
    '''
    Calculates the product of the numbers from a list
    :param lst: the list of natural numbers
    :return: the product of the numbers from the list
    '''
    rez = 1
    for i in lst:
        rez = rez*i
    return rez

def get_cmmdc_v1(x, y):
    '''
    Calculates the greatest common divisor of two numbers
    :param x: first number
    :param y: second number
    :return: greatest common divisor of x and y
    '''
    if y==0 : return int(x)
    return get_cmmdc_v1(y,int(int(x)%int(y)))


def get_cmmdc_v2(x, y):
    '''
    Calculates the greatest common divisor of two numbers
    :param x: first number
    :param y: second number
    :return: greatest common divisor of x and y
    '''
    while x!=y :
        if int(x)>int(y): x=int(x)-int(y)
        if int(y)>int(x): y=int(y)-int(x)
    return x

assert is_prime(3) == True
assert is_prime(5) == True

assert get_cmmdc_v1(15, 5) == 5
assert get_cmmdc_v2(25,10) == 5

def main():
    while True:
        print("What algorithm you want to run?")
        print("1. Check if a number is prime")
        print("2. Number product from a list")
        print("3. Greatest common divisor of two numbers using the first algorithm")
        print("4. Greatest common divisor of two numbers using the second algorithm")
        print("5. Exit")
        option = input("Select the number of the algorithm: ")
        # 2383 codul, problemele 3 si 4
        if option == "1":
            n = input("Type the number: ")
            print(is_prime(n))

        if option == "2":
            print("Type the number of numbers: ", end = " ")
            n = input()
            print("Type the numbers: ", end = " ")
            lst = list(map(int, input().split()))
            print(get_product(lst))

        if option == "3":
            print("Type the numbers:", end = " ")
            x, y = input().split()
            print(get_cmmdc_v1(x,y))

        if option == "4":
            print("Type the numbers:", end=" ")
            x, y = input().split()
            print(get_cmmdc_v2(x,y))

        if option == "5":
            break
        print()

if __name__ == '__main__':
    main()