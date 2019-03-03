

#: comparator functions

def _greater_than(a, b):
    return a > b


#: sorting functions


def bubble_sort(array, key=_greater_than):

    N = len(array)

    if N <= 1:
        return array

    for outer in range(N - 1, 0, -1):
        for inner in range(outer):
            i0, i1 = inner, inner + 1
            if key(array[i0], array[i1]):
                array[i0], array[i1] = (
                    array[i1], array[i0]
                    )

    return array


def insertion_sort(array, key=_greater_than):

    N = len(array)

    if N <= 1:
        return array

    for i in range(N - 1, 1, -1):
        i0, i1 = i, i - 1
        while key(array[i1], array[i0]):
            array[i0], array[i1] = (
                    array[i1], array[i0]
                    )

    return array


def selection_sort(array, key=_greater_than):

    N = len(array)

    if N <= 1:
        return array

    for i in range(N - 1):
        min_elem = array[i]
        min_idx = i
        for j in range(i + 1, N):
            if key(min_elem, array[j]):
                min_elem = array[j]
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


def quick_sort(array, key=_greater_than):
    """ Implementation of quicksort

    pivot chosen as first element for now
    """

    N = len(array)

    if N <= 1:
        return array

    pivot_idx = 0
    pivot = array[pivot_idx]
    array[0], array[pivot_idx] = array[pivot_idx], array[0]

    k = 1
    ptr = N - 1
    for _ in range(1, N):
        # element is greater than pivot
        if key(array[k], pivot):
            array[k], array[ptr] = array[ptr], array[k]
            ptr -= 1
        # element is less than pivot
        else:
            k += 1

    array = quick_sort(array[1:k]) + [pivot] + quick_sort(array[k:])

    return array

#: for testing


def _main():

    from random import shuffle

    arr = list(range(20))

    print()

    print("true\n", arr, sep='')
    shuffle(arr)
    print("shuffled\n", arr, '\n', sep='')

    print("baseline")
    print(sorted(arr[:]))
    print("bubble_sort")
    print(bubble_sort(arr[:]))
    print("insertion_sort")
    print(insertion_sort(arr[:]))
    print("selection_sort")
    print(selection_sort(arr[:]))
    print("quick_sort")
    print(quick_sort(arr[:]))

    print()


if __name__ == "__main__":
    _main()
