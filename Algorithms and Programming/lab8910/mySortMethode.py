def mySort(iterable, *, key=lambda x: x, reverse=False):
    '''
    Functia proprie de sortare cu interfata similara functiei sorted
    Sortare folosind algoritmul bubblesort
    :param iterable: lista pe care o sorteaza
    :param key: metoda de sortare
    :param reverse: sortare crescatoare/descrescatoare dupa metoda
    :return: lista sortata
    '''
    isSorted = False
    while isSorted is not True:
        isSorted = True
        for i in range(len(iterable) - 1):
            if key(iterable[i] > iterable[i+1]):
                iterable[i], iterable[i+1] = iterable[i+1], iterable[i]
                isSorted = False
        if not reverse:
            return iterable
        else:
            return list(reversed(iterable))
