def bubble_sort(a):
    if len(a) == 1:
        return a
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a


if __name__ == "__main__":
    a = [34, 5, 6, 1, 1, 75, 100, 3, 1]
    print bubble_sort(a)
