def selection_sort(a):
    if len(a) == 1:
        return a
    for i in range(0, len(a)):
        maximum = a[0]
        index = 0
        for j in range(0, len(a) - i):
            if a[j] > maximum:
                maximum = a[j]
                index = j
        a[index], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[index]
    return a


if __name__ == "__main__":
    a = [34, 5, 6, 1, 1, 75, 100, 3, 1, -18]
    print selection_sort(a)
