def radix_sort(a):
    buckets = [[], [], [], [], [], [], [], [], [], []]
    size = len(str(max(a)))
    for i in range(1, size + 1):
        modulus = pow(10, i)
        div = pow(10, i - 1)
        if i > 1:
            index = 0
            for x in buckets:
                for y in x:
                    a[index] = y
                    index += 1
            buckets = [[], [], [], [], [], [], [], [], [], []]
        for j in range(0, len(a)):
            place_value = float(a[j] % modulus) / div
            buckets[int(place_value)].append(a[j])
    index = 0
    for x in buckets:
        for y in x:
            a[index] = y
            index += 1
    return a


if __name__ == "__main__":
    a = [0, 70, 60, 100, 100000000, 10, 1000, 1000]
    print radix_sort(a)
