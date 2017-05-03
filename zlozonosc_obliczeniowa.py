import time
from functools import wraps

PROF_DATA = {}


def profile(fn):
    @wraps(fn)
    def with_profiling(*args, **kwargs):
        start_time = time.time()

        ret = fn(*args, **kwargs)

        elapsed_time = time.time() - start_time

        if fn.__name__ not in PROF_DATA:
            PROF_DATA[fn.__name__] = [0, []]
        PROF_DATA[fn.__name__][0] += 1
        PROF_DATA[fn.__name__][1].append(elapsed_time)
        return ret

    return with_profiling


def print_prof_data():
    global avg_time
    for fname, data in PROF_DATA.items():
        max_time = max(data[1])
        avg_time = sum(data[1]) / len(data[1])
        # print("Function %s called %d times. " % (fname, data[0])),
        # print('Execution time max: %.3f, average: %.3f' % (max_time, avg_time))
        # print('time = %.3f' % (avg_time))


def clear_prof_data():
    global PROF_DATA
    PROF_DATA = {}


@profile
def algorithm(size):
    # copy here your algorithm
    import random

    def losuj(size, do):  # zwraca tablicę o podanym rozmiarze
        tab = []  # z wylosowanymi wartościami
        while size > 0:  # dopóki jakieś musi dodać
            tmp = random.randint(0, do)
            tab.append(tmp)
            size -= 1  # zmniejsza ilość pozostałych komórek do wylosowania
        return tab

    # BUBBLESORT
    def sort(tab):  # zwraca posortowaną tablicę
        for i in range(len(tab)):
            j = len(tab) - 1  # od ostatniej komórki
            while j > i:  # do aktualnie szukanej jako najmniejsza
                if tab[j] < tab[j - 1]:  # jeśli komórka wcześniej jest mniejsza, zamienia
                    tmp = tab[j]
                    tab[j] = tab[j - 1]
                    tab[j - 1] = tmp
                j -= 1
        return tab

    # QUICKSORT
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
    def algorithm_n_to_3():
        a = 0
        for i in range(0, size):
            for j in range(0, size):
                for k in range(0, size):
                    a += 1

    tab = losuj(size, 100000)
    tab = quicksort(tab, 0, len(tab) - 1)
    # tab = sort(tab)
    # algorithm_n_to_3()


def check_exp_to_r(points, middle_point, step, r):
    c = (points[middle_point][1] ** (1 / r)) / points[middle_point][0]
    print("c = " + str(c))
    for i in range(0, (size_max - size_min) // step):
        ratio = ((c * points[i][0]) ** r) / points[i][1]
        if (abs(ratio - 1) > 0.15):
            print("Too high difference r = " + str(r))
            print("ratio = " + str(ratio) + "    point = " + str(points[i][0]) + " " + str(points[i][1]))
            return False
    print("It's a O(n^" + str(r) + ") with c = " + str(c))
    return True


def set_points(size_min, size_max, step):
    height = (size_max - size_min) // step
    # points[][0] = size
    # points[][1] = avg_time * 1000
    points = [[0 for x in range(2)] for y in range(height + 1)]  # matrix
    counter = 0
    for size in range(size_min, size_max, step):
        # how many times algorithm should be run for one size
        # higher number = higher precision
        precision = 1
        for i in range(0, precision + 1):
            algorithm(size)
        print_prof_data()
        clear_prof_data()
        print('%d, %.3f' % (size, avg_time * 1000))
        points[counter][0] = size
        points[counter][1] = avg_time * 1000
        counter += 1
    return points


size_max = 100000
size_min = 10000
r = 1
step = (size_max - size_min) // 10  # 10 points

points = set_points(size_min, size_max, step)
middle_point = ((size_max - size_min) // step + 1) // 2
print("middle point = (" + str(points[middle_point][0]) + ", " + str(points[middle_point][1]) + ")")
while (check_exp_to_r(points, middle_point, step, r) == False and r < 6):
    r += 1
