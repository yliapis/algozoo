

def bubble_sort(array, key=lambda a, b: a > b):

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


def insertion_sort(array, key=lambda a, b: a > b):

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


if __name__ == "__main__":

    from numpy.random import permutation

    arr = permutation(20)

    print(arr)
    print(sorted(arr))
    print(bubble_sort(arr))
    print(insertion_sort(arr))
