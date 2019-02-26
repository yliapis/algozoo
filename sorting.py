

def _greater_than(a, b):
    return a > b


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
        base_idx = i
        min_idx = 0
        for j in range(i, N):
            if not key(array[i], array[j]):
                min_idx = j
        array[base_idx], array[min_idx] = (
                    array[base_idx], array[min_idx]
                    )

    return array



if __name__ == "__main__":

    from numpy.random import permutation

    arr = permutation(20)

    print(arr)
    print(sorted(arr))
    print(bubble_sort(arr))
    print(insertion_sort(arr))
    print(selection_sort(arr))
