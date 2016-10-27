def insertion_sort(a):
    if len(a) == 1:
        return a
    for i in range(1, len(a)):
        j = i
        while (j >= 1 and a[j] < a[j - 1]):
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
    return a


if __name__ == "__main__":
    a = [34, 5, 6, 1, 1, 75, 100, 3, 1, -18,0,-45]
    print insertion_sort(a)
