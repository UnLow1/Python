import random


def generate_args_bubblesort(size):
    return rand(size, 10000)


def generate_args_n3(size):
    return size


def generate_args_quicksort(size):
    list = rand(size, 10000)
    return list, 0, (len(list) - 1)


def generate_args_hanoi(size):
    a = []
    for i in range(0, size):
        a.append(size - i)
    return size, a, [], []


def generate_args_bin_search(size):
    list = rand(size, 10000)
    return list[random.randint(0, len(list) - 1)], list


def rand(size, do):  # zwraca tablicę o podanym rozmiarze
    tab = []  # z wylosowanymi wartościami
    while size > 0:  # dopóki jakieś musi dodać
        tmp = random.randint(0, do)
        tab.append(tmp)
        size -= 1  # zmniejsza ilość pozostałych komórek do wylosowania
    return tab


# BUBBLESORT O(n^2)
def bubblesort(tab):  # zwraca posortowaną tablicę
    for i in range(len(tab)):
        j = len(tab) - 1  # od ostatniej komórki
        while j > i:  # do aktualnie szukanej jako najmniejsza
            if tab[j] < tab[j - 1]:
                tmp = tab[j]
                tab[j] = tab[j - 1]
                tab[j - 1] = tmp
            j -= 1
    return tab


# QUICKSORT O(n^1)     should be O(nlog(n))
def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot - 1)
        quicksort(myList, pivot + 1, end)
    return myList


def partition(myList, start, end):
    pivot = myList[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            # swap places
            temp = myList[left]
            myList[left] = myList[right]
            myList[right] = temp
    # swap start with myList[right]
    temp = myList[start]
    myList[start] = myList[right]
    myList[right] = temp
    return right


# ALGORITH O(n^3)
def algorithm_n_to_3(size):
    a = 0
    for i in range(0, size):
        for j in range(0, size):
            for k in range(0, size):
                a += 1


# BINARY SEARCH O(log(n))
def binary_search(value, data):
    left = 0
    right = len(data) - 1
    # szukaj dopoki granica lewa jest mniejsza od prawej
    while left < right:
        middle = (left + right) // 2  # wybor elementu srodkowego
        if data[middle] < value:
            left = middle + 1  # to odrzuc lewa polowke (przesun lewa granice)
        else:  # w przeciwnym razie
            right = middle  # odrzuc prawa polowke (przesun prawa granice)
    # sprawdz czy znaleziono szukany element
    if data[right] == value:
        return right
    else:
        return None


# HANOI TOWERS O(2^n)
def hanoi(n, A, B, C):
    if n == 1:
        C.append(A.pop())
    else:
        hanoi(n - 1, A, C, B)  # hanoi automatycznie ukazuje
        C.append(A.pop())
        hanoi(n - 1, B, A, C)

        # quicksort(tab, 0, len(tab) - 1)
        # bubblesort(tab)
        # algorithm_n_to_3(size)
        # binary_search(tab[random.randint(0, len(tab) - 1)], tab)
        # hanoi(size, a, [], [])
